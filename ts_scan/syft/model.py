# generated by datamodel-codegen:
#   filename:  schema-16.0.18.json
#   timestamp: 2024-10-16T16:17:37+00:00

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

from pydantic import AwareDatetime, BaseModel, Field, RootModel, constr


class CConanFileEntry(BaseModel):
    ref: str


class CConanInfoEntry(BaseModel):
    ref: str
    package_id: Optional[str] = None


class CConanLockV2Entry(BaseModel):
    ref: str
    packageID: Optional[str] = None
    username: Optional[str] = None
    channel: Optional[str] = None
    recipeRevision: Optional[str] = None
    packageRevision: Optional[str] = None
    timestamp: Optional[str] = None


class CPE(BaseModel):
    cpe: str
    source: Optional[str] = None


class CocoaPodfileLockEntry(BaseModel):
    checksum: str


class Coordinates(BaseModel):
    path: str
    layerID: Optional[str] = None


class DartPubspecLockEntry(BaseModel):
    name: str
    version: str
    hosted_url: Optional[str] = None
    vcs_url: Optional[str] = None


class Descriptor(BaseModel):
    name: str
    version: str
    configuration: Optional[Any] = None


class Digest(BaseModel):
    algorithm: str
    value: str


class DotnetDepsEntry(BaseModel):
    name: str
    version: str
    path: str
    sha512: str
    hashPath: str


class DotnetPortableExecutableEntry(BaseModel):
    assemblyVersion: str
    legalCopyright: str
    comments: Optional[str] = None
    internalName: Optional[str] = None
    companyName: str
    productName: str
    productVersion: str


class DpkgFileRecord(BaseModel):
    path: str
    digest: Optional[Digest] = None
    isConfigFile: bool


class ELFSecurityFeatures(BaseModel):
    symbolTableStripped: bool
    stackCanary: Optional[bool] = None
    nx: bool
    relRO: str
    pie: bool
    dso: bool
    safeStack: Optional[bool] = None
    cfi: Optional[bool] = None
    fortify: Optional[bool] = None


class ElfBinaryPackageNoteJsonPayload(BaseModel):
    type: Optional[str] = None
    architecture: Optional[str] = None
    osCPE: Optional[str] = None
    os: Optional[str] = None
    osVersion: Optional[str] = None
    system: Optional[str] = None
    vendor: Optional[str] = None
    sourceRepo: Optional[str] = None
    commit: Optional[str] = None


class ElixirMixLockEntry(BaseModel):
    name: str
    version: str
    pkgHash: str
    pkgHashExt: str


class ErlangRebarLockEntry(BaseModel):
    name: str
    version: str
    pkgHash: str
    pkgHashExt: str


class Executable(BaseModel):
    format: str
    hasExports: bool
    hasEntrypoint: bool
    importedLibraries: List[str]
    elfSecurityFeatures: Optional[ELFSecurityFeatures] = None


class FileLicenseEvidence(BaseModel):
    confidence: int
    offset: int
    extent: int


class FileMetadataEntry(BaseModel):
    mode: int
    type: str
    linkDestination: Optional[str] = None
    userID: int
    groupID: int
    mimeType: str
    size: int


class GoModuleEntry(BaseModel):
    h1Digest: Optional[str] = None


class HaskellHackageStackEntry(BaseModel):
    pkgHash: Optional[str] = None


class HaskellHackageStackLockEntry(BaseModel):
    pkgHash: Optional[str] = None
    snapshotURL: Optional[str] = None


class IDLikes(RootModel[List[str]]):
    root: List[str]


class JavaPomParent(BaseModel):
    groupId: str
    artifactId: str
    version: str


class JavaPomProject(BaseModel):
    path: str
    parent: Optional[JavaPomParent] = None
    groupId: str
    artifactId: str
    version: str
    name: str
    description: Optional[str] = None
    url: Optional[str] = None


class JavaPomProperties(BaseModel):
    path: str
    name: str
    groupId: str
    artifactId: str
    version: str
    scope: Optional[str] = None
    extraFields: Optional[Dict[constr(pattern=r'.*'), str]] = None


class JavaVMRelease(BaseModel):
    implementor: Optional[str] = None
    implementorVersion: Optional[str] = None
    javaRuntimeVersion: Optional[str] = None
    javaVersion: Optional[str] = None
    javaVersionDate: Optional[str] = None
    libc: Optional[str] = None
    modules: Optional[List[str]] = None
    osArch: Optional[str] = None
    osName: Optional[str] = None
    osVersion: Optional[str] = None
    source: Optional[str] = None
    buildSource: Optional[str] = None
    buildSourceRepo: Optional[str] = None
    sourceRepo: Optional[str] = None
    fullVersion: Optional[str] = None
    semanticVersion: Optional[str] = None
    buildInfo: Optional[str] = None
    jvmVariant: Optional[str] = None
    jvmVersion: Optional[str] = None
    imageType: Optional[str] = None
    buildType: Optional[str] = None


class JavascriptNpmPackage(BaseModel):
    name: str
    version: str
    author: str
    homepage: str
    description: str
    url: str
    private: bool


class JavascriptNpmPackageLockEntry(BaseModel):
    resolved: str
    integrity: str


class JavascriptYarnLockEntry(BaseModel):
    resolved: str
    integrity: str


class KeyValue(BaseModel):
    key: str
    value: str


class KeyValues(RootModel[List[KeyValue]]):
    root: List[KeyValue]


class LinuxKernelArchive(BaseModel):
    name: str
    architecture: str
    version: str
    extendedVersion: Optional[str] = None
    buildTime: Optional[str] = None
    author: Optional[str] = None
    format: Optional[str] = None
    rwRootFS: Optional[bool] = None
    swapDevice: Optional[int] = None
    rootDevice: Optional[int] = None
    videoMode: Optional[str] = None


class LinuxKernelModuleParameter(BaseModel):
    type: Optional[str] = None
    description: Optional[str] = None


class LinuxRelease(BaseModel):
    prettyName: Optional[str] = None
    name: Optional[str] = None
    id: Optional[str] = None
    idLike: Optional[IDLikes] = None
    version: Optional[str] = None
    versionID: Optional[str] = None
    versionCodename: Optional[str] = None
    buildID: Optional[str] = None
    imageID: Optional[str] = None
    imageVersion: Optional[str] = None
    variant: Optional[str] = None
    variantID: Optional[str] = None
    homeURL: Optional[str] = None
    supportURL: Optional[str] = None
    bugReportURL: Optional[str] = None
    privacyPolicyURL: Optional[str] = None
    cpeName: Optional[str] = None
    supportEnd: Optional[str] = None


class Location(BaseModel):
    path: str
    layerID: Optional[str] = None
    accessPath: str
    annotations: Optional[Dict[constr(pattern=r'.*'), str]] = None


class LuarocksPackage(BaseModel):
    name: str
    version: str
    license: str
    homepage: str
    description: str
    url: str
    dependencies: Dict[constr(pattern=r'.*'), str]


class MicrosoftKbPatch(BaseModel):
    product_id: str
    kb: str


class NixStoreEntry(BaseModel):
    outputHash: str
    output: Optional[str] = None
    files: List[str]


class OpamPackage(BaseModel):
    name: str
    version: str
    licenses: List[str]
    url: str
    checksum: List[str]
    homepage: str
    dependencies: List[str]


class PhpComposerAuthors(BaseModel):
    name: str
    email: Optional[str] = None
    homepage: Optional[str] = None


class PhpComposerExternalReference(BaseModel):
    type: str
    url: str
    reference: str
    shasum: Optional[str] = None


class PhpComposerInstalledEntry(BaseModel):
    name: str
    version: str
    source: PhpComposerExternalReference
    dist: PhpComposerExternalReference
    require: Optional[Dict[constr(pattern=r'.*'), str]] = None
    provide: Optional[Dict[constr(pattern=r'.*'), str]] = None
    require_dev: Optional[Dict[constr(pattern=r'.*'), str]] = Field(
        None, alias='require-dev'
    )
    suggest: Optional[Dict[constr(pattern=r'.*'), str]] = None
    license: Optional[List[str]] = None
    type: Optional[str] = None
    notification_url: Optional[str] = Field(None, alias='notification-url')
    bin: Optional[List[str]] = None
    authors: Optional[List[PhpComposerAuthors]] = None
    description: Optional[str] = None
    homepage: Optional[str] = None
    keywords: Optional[List[str]] = None
    time: Optional[str] = None


class PhpComposerLockEntry(BaseModel):
    name: str
    version: str
    source: PhpComposerExternalReference
    dist: PhpComposerExternalReference
    require: Optional[Dict[constr(pattern=r'.*'), str]] = None
    provide: Optional[Dict[constr(pattern=r'.*'), str]] = None
    require_dev: Optional[Dict[constr(pattern=r'.*'), str]] = Field(
        None, alias='require-dev'
    )
    suggest: Optional[Dict[constr(pattern=r'.*'), str]] = None
    license: Optional[List[str]] = None
    type: Optional[str] = None
    notification_url: Optional[str] = Field(None, alias='notification-url')
    bin: Optional[List[str]] = None
    authors: Optional[List[PhpComposerAuthors]] = None
    description: Optional[str] = None
    homepage: Optional[str] = None
    keywords: Optional[List[str]] = None
    time: Optional[str] = None


class PhpPeclEntry(BaseModel):
    name: str
    version: str
    license: Optional[List[str]] = None


class PortageFileRecord(BaseModel):
    path: str
    digest: Optional[Digest] = None


class PythonDirectURLOriginInfo(BaseModel):
    url: str
    commitId: Optional[str] = None
    vcs: Optional[str] = None


class PythonFileDigest(BaseModel):
    algorithm: str
    value: str


class PythonFileRecord(BaseModel):
    path: str
    digest: Optional[PythonFileDigest] = None
    size: Optional[str] = None


class PythonPackage(BaseModel):
    name: str
    version: str
    author: str
    authorEmail: str
    platform: str
    files: Optional[List[PythonFileRecord]] = None
    sitePackagesRootPath: str
    topLevelPackages: Optional[List[str]] = None
    directUrlOrigin: Optional[PythonDirectURLOriginInfo] = None
    requiresPython: Optional[str] = None
    requiresDist: Optional[List[str]] = None
    providesExtra: Optional[List[str]] = None


class PythonPipRequirementsEntry(BaseModel):
    name: str
    extras: Optional[List[str]] = None
    versionConstraint: str
    url: Optional[str] = None
    markers: Optional[str] = None


class PythonPipfileLockEntry(BaseModel):
    hashes: List[str]
    index: str


class PythonPoetryLockDependencyEntry(BaseModel):
    name: str
    version: str
    optional: bool
    markers: Optional[str] = None
    extras: Optional[List[str]] = None


class PythonPoetryLockExtraEntry(BaseModel):
    name: str
    dependencies: List[str]


class RDescription(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    maintainer: Optional[str] = None
    url: Optional[List[str]] = None
    repository: Optional[str] = None
    built: Optional[str] = None
    needsCompilation: Optional[bool] = None
    imports: Optional[List[str]] = None
    depends: Optional[List[str]] = None
    suggests: Optional[List[str]] = None


class Relationship(BaseModel):
    parent: str
    child: str
    type: str
    metadata: Optional[Any] = None


class RpmFileRecord(BaseModel):
    path: str
    mode: int
    size: int
    digest: Digest
    userName: str
    groupName: str
    flags: str


class RubyGemspec(BaseModel):
    name: str
    version: str
    files: Optional[List[str]] = None
    authors: Optional[List[str]] = None
    homepage: Optional[str] = None


class RustCargoAuditEntry(BaseModel):
    name: str
    version: str
    source: str


class RustCargoLockEntry(BaseModel):
    name: str
    version: str
    source: str
    checksum: str
    dependencies: List[str]


class Schema(BaseModel):
    version: str
    url: str


class Source(BaseModel):
    id: str
    name: str
    version: str
    type: str
    metadata: Any


class SwiftPackageManagerLockEntry(BaseModel):
    revision: str


class SwiplpackPackage(BaseModel):
    name: str
    version: str
    author: str
    authorEmail: str
    packager: str
    packagerEmail: str
    homepage: str
    dependencies: List[str]


class WordpressPluginEntry(BaseModel):
    pluginInstallDirectory: str
    author: Optional[str] = None
    authorUri: Optional[str] = None


class Cpes(RootModel[List[CPE]]):
    root: List[CPE]


class AlpmFileRecord(BaseModel):
    path: Optional[str] = None
    type: Optional[str] = None
    uid: Optional[str] = None
    gid: Optional[str] = None
    time: Optional[AwareDatetime] = None
    size: Optional[str] = None
    link: Optional[str] = None
    digest: Optional[List[Digest]] = None


class ApkFileRecord(BaseModel):
    path: str
    ownerUid: Optional[str] = None
    ownerGid: Optional[str] = None
    permissions: Optional[str] = None
    digest: Optional[Digest] = None


class CConanLockEntry(BaseModel):
    ref: str
    package_id: Optional[str] = None
    prev: Optional[str] = None
    requires: Optional[List[str]] = None
    build_requires: Optional[List[str]] = None
    py_requires: Optional[List[str]] = None
    options: Optional[KeyValues] = None
    path: Optional[str] = None
    context: Optional[str] = None


class ClassifierMatch(BaseModel):
    classifier: str
    location: Location


class DpkgDbEntry(BaseModel):
    package: str
    source: str
    version: str
    sourceVersion: str
    architecture: str
    maintainer: str
    installedSize: int
    provides: Optional[List[str]] = None
    depends: Optional[List[str]] = None
    preDepends: Optional[List[str]] = None
    files: List[DpkgFileRecord]


class FileLicense(BaseModel):
    value: str
    spdxExpression: str
    type: str
    evidence: Optional[FileLicenseEvidence] = None


class GoModuleBuildinfoEntry(BaseModel):
    goBuildSettings: Optional[KeyValues] = None
    goCompiledVersion: str
    architecture: str
    h1Digest: Optional[str] = None
    mainModule: Optional[str] = None
    goCryptoSettings: Optional[List[str]] = None
    goExperiments: Optional[List[str]] = None


class JavaJvmInstallation(BaseModel):
    release: JavaVMRelease
    files: List[str]


class JavaManifest(BaseModel):
    main: Optional[KeyValues] = None
    sections: Optional[List[KeyValues]] = None


class License(BaseModel):
    value: str
    spdxExpression: str
    type: str
    urls: List[str]
    locations: List[Location]


class LinuxKernelModule(BaseModel):
    name: Optional[str] = None
    version: Optional[str] = None
    sourceVersion: Optional[str] = None
    path: Optional[str] = None
    description: Optional[str] = None
    author: Optional[str] = None
    license: Optional[str] = None
    kernelVersion: Optional[str] = None
    versionMagic: Optional[str] = None
    parameters: Optional[Dict[constr(pattern=r'.*'), LinuxKernelModuleParameter]] = None


class PortageDbEntry(BaseModel):
    installedSize: int
    files: List[PortageFileRecord]


class PythonPoetryLockEntry(BaseModel):
    index: str
    dependencies: List[PythonPoetryLockDependencyEntry]
    extras: Optional[List[PythonPoetryLockExtraEntry]] = None


class RpmArchive(BaseModel):
    name: str
    version: str
    epoch: Optional[int] = None
    architecture: str
    release: str
    sourceRpm: str
    size: int
    vendor: str
    modularityLabel: Optional[str] = None
    provides: Optional[List[str]] = None
    requires: Optional[List[str]] = None
    files: List[RpmFileRecord]


class RpmDbEntry(BaseModel):
    name: str
    version: str
    epoch: Optional[int] = None
    architecture: str
    release: str
    sourceRpm: str
    size: int
    vendor: str
    modularityLabel: Optional[str] = None
    provides: Optional[List[str]] = None
    requires: Optional[List[str]] = None
    files: List[RpmFileRecord]


class Licenses(RootModel[List[License]]):
    root: List[License]


class AlpmDbEntry(BaseModel):
    basepackage: str
    package: str
    version: str
    description: str
    architecture: str
    size: int
    packager: str
    url: str
    validation: str
    reason: int
    files: List[AlpmFileRecord]
    backup: List[AlpmFileRecord]
    provides: Optional[List[str]] = None
    depends: Optional[List[str]] = None


class ApkDbEntry(BaseModel):
    package: str
    originPackage: str
    maintainer: str
    version: str
    architecture: str
    url: str
    description: str
    size: int
    installedSize: int
    pullDependencies: List[str]
    provides: List[str]
    pullChecksum: str
    gitCommitOfApkPort: str
    files: List[ApkFileRecord]


class BinarySignature(BaseModel):
    matches: List[ClassifierMatch]


class File(BaseModel):
    id: str
    location: Coordinates
    metadata: Optional[FileMetadataEntry] = None
    contents: Optional[str] = None
    digests: Optional[List[Digest]] = None
    licenses: Optional[List[FileLicense]] = None
    executable: Optional[Executable] = None
    unknowns: Optional[List[str]] = None


class JavaArchive(BaseModel):
    virtualPath: str
    manifest: Optional[JavaManifest] = None
    pomProperties: Optional[JavaPomProperties] = None
    pomProject: Optional[JavaPomProject] = None
    digest: Optional[List[Digest]] = None


class Package(BaseModel):
    id: str
    name: str
    version: str
    type: str
    foundBy: str
    locations: List[Location]
    licenses: Licenses
    language: str
    cpes: Cpes
    purl: str
    metadataType: Optional[str] = None
    metadata: Optional[
        Union[
            AlpmDbEntry,
            ApkDbEntry,
            BinarySignature,
            CConanFileEntry,
            CConanInfoEntry,
            CConanLockEntry,
            CConanLockV2Entry,
            CocoaPodfileLockEntry,
            DartPubspecLockEntry,
            DotnetDepsEntry,
            DotnetPortableExecutableEntry,
            DpkgDbEntry,
            ElfBinaryPackageNoteJsonPayload,
            ElixirMixLockEntry,
            ErlangRebarLockEntry,
            GoModuleBuildinfoEntry,
            GoModuleEntry,
            HaskellHackageStackEntry,
            HaskellHackageStackLockEntry,
            JavaArchive,
            JavaJvmInstallation,
            JavascriptNpmPackage,
            JavascriptNpmPackageLockEntry,
            JavascriptYarnLockEntry,
            LinuxKernelArchive,
            LinuxKernelModule,
            LuarocksPackage,
            MicrosoftKbPatch,
            NixStoreEntry,
            OpamPackage,
            PhpComposerInstalledEntry,
            PhpComposerLockEntry,
            PhpPeclEntry,
            PortageDbEntry,
            PythonPackage,
            PythonPipRequirementsEntry,
            PythonPipfileLockEntry,
            PythonPoetryLockEntry,
            RDescription,
            RpmArchive,
            RpmDbEntry,
            RubyGemspec,
            RustCargoAuditEntry,
            RustCargoLockEntry,
            SwiftPackageManagerLockEntry,
            SwiplpackPackage,
            WordpressPluginEntry,
        ]
    ] = None


class Document(BaseModel):
    artifacts: List[Package]
    artifactRelationships: List[Relationship]
    files: Optional[List[File]] = None
    source: Source
    distro: LinuxRelease
    descriptor: Descriptor
    schema_: Schema = Field(..., alias='schema')


class Model(RootModel[Document]):
    root: Document
