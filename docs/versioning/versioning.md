@"
# GrayProject Versioning Convention

## Official Version Format

GrayProject official releases use:

v<major>.<minor>.<patch>-U

Example:

v0.0.1-U

Where:

-U means Uolrier Official.

## Version Meaning

Major:
- Large architecture changes

Minor:
- New major features

Patch:
- Bug fixes and small improvements

## Git Tag Convention

Official releases use:

v0.0.1-U

Example:

git tag -a v0.0.1-U -m "GrayProject official release v0.0.1-U"

## Release Naming

Official releases should use:

GrayProject v0.0.1-U

Community or custom versions should not use the -U suffix.
"@ | Set-Content docs\versioning\versioning.md