# Scanning for crypto algorithms

**ts-scan** also supports to scan for crypto algorithms. Using the deepscan extension ***pyminr***, which ia a wrapper around the **minr** implementation by SCANOSS, DeepScan is able to assess files for known encryption implementations.

Encryption analysis is enabled by default. There are two options for the crypto analysis:

* *Analysis of a directory content.* Can be useful when only the source code from a directory has to be scanned

* *Analysis of the dependencies files.* In this case files of every dependency from a dependecy scan will be analysed as long as they are available. 

For example, after scanning a Maven project one can look for used encryption algorithms in the sources of every package as long as they are available in the Maven repository (For most OS packages hosten on Maven Central this will be the case).

> [!NOTE]
>
> Our SCANOSS integration provides two sorts of usage. The first is the default option, using the public knowledge base. The second is to use your private API key and access either a private endpoint or the commercial subscription. SCANOSS does not provide different datasets. The public will be updated in different timelines than the pcomemrcial one. But the major difference are the API limits. The burst rate is much higher in the subscriptions than in the public API. [Reach out](https://www.trustsource.io/contact) to learn more, in case you are interested.  
>

## Analysis of a directory content

```shell
ts-scan analyse -o scan.json <DIRECTORY>
```


## Analysis of the dependencies files

Scan a directory for dependencies first and store results into the ```scan.json``` file.

```shell
ts-scan scan -o scan.json <DIRECTORY>
```

Next, analyse every depedency from the scan and store the scan together with analysis results into the ```scan.analysed.json``` 

```shell
ts-scan analyse -o scan.analysed.json scan.json
```

## Analysis results

The analysis results can be found in the output file. The output file contains the original dependency scan as well as a ```deepscans``` section containing results for each dependency.  The following example shows a snippet from the scanning results of a Maven projects containing the ```mvn:org.apache.httpcomponents:httpclient``` dependency:

```json
{
  ...
  "deepscans": [
    ...
      "mvn:org.apache.httpcomponents:httpclient": {
        "results": {
          ...
          "httpclient-4.5.14-sources/org/apache/http/impl/auth/DigestScheme.java": {
            "crypto": [
              {
                "algorithm": "MD5",
                "coding": 128
              }
              ...
            ]
          },
          ...
        }
    ...
  ]
}

```

If some usage of an encryption algorithm is found in a source file, it appears in the results dictionary of that file under ```crypto``` category. In this case a possible usage of an ```MD5``` algorithm was found in the ```org/apache/http/impl/auth/DigestScheme.java``` in the ```org.apache.httpcomponents:httpclient``` package.  

> [!NOTE]
>
> If several analysers found results all results will appear in that dictionary but every analyser will have a separate category.

