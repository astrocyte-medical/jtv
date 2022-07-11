[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-teal.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](https://opensource.org/licenses/MIT)


# jtv

jtv is a command line utility which allows you to visualise JSON and YAML schemas as text trees. It may be used as a complement to `jq`, to facilitate the interpretation of a JSON schema, prior to defining filters.

## Installation

Use a virtual environment. From PyPI:

```
$ pip install --upgrade pip
$ pip install -i https://test.pypi.org/simple/ jtv==1.71.0
```

From source:
```
$ python setup.py install
```

## Usage

To show the help use `jtv -h`

![help](https://user-images.githubusercontent.com/80931870/178188951-3907c353-c5ad-4c09-9c60-75004a7bb921.png)

## Inconsistency handling

Arrays may contain objects with different schemas. By default, or using the option `--mode distinct` will wrapp all objects in a new object with the node key specifying a schema version. The appended `◎-schema-0` node does not exist in the JSON and is strictly used to differentiate between different object schemas. 

```
$ echo '[{"0": {"00": [{"000": "", "001": true, "002": []}, {"NEW": {"A": 2}}]}, "1": {"10": []}}, {"A": {"r": []}}]' | jtv -s --mode distinct
```

![mode-distinct](https://user-images.githubusercontent.com/80931870/178188961-034e9947-aa11-4453-8e58-2aebeb788f36.png)

To display all the nodes from each distinct object under a single object, use `--mode union`. 

```
$ echo '[{"0": {"00": [{"000": "", "001": true, "002": []}, {"NEW": {"A": 2}}]}, "1": {"10": []}}, {"A": {"r": []}}]' | jtv -s --mode union
```

![mode-union](https://user-images.githubusercontent.com/80931870/178188978-ff786d50-8721-4432-b3eb-dd086b1c61e7.png)

To display only the schema of the first object use `--mode first`. 

```
$ echo '[{"0": {"00": [{"000": "", "001": true, "002": []}, {"NEW": {"A": 2}}]}, "1": {"10": []}}, {"A": {"r": []}}]' | jtv -s --mode first
```

![mode-first](https://user-images.githubusercontent.com/80931870/178188971-edc49b72-98bc-462f-ab5d-0d5821fa29b9.png)

To visualise JSON schemas, as above, use the `-s` flag. To visualise YAML schema use the `-y` flag.

```
$ cat .gitlab-ci.yml | jtv -y
```

![yaml](https://user-images.githubusercontent.com/80931870/178189002-98875801-984a-4d9c-b75d-c7bbefe1e9f8.png)


## Tests
Run `tox` in the root project directory.

## Development

Increment version:
```
bumpver update --minor
```

