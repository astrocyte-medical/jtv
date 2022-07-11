# command_io.py
from jtv import __version__


# Inputs
invalid_json = '[}"ivnadil{:"'
invalid_yaml = '''\
root_node: ]
'''
valid_yaml = '''\
root_node:
  name: root
  nested_node:
    name: nested_node
  array:
    - node0
    - node1
'''
object_empty_root_node_json = '{}'
object_empty_nested_node_json = '{"object": {}}'
list_empty_root_node_json = '[]'
list_empty_nested_node_json = '{"list": []}'
string_empty_node_json = '{"string": ""}'
object_node_and_types_json = '{"object": {"array": [], "string": "Hello, World!", "boolean": true, "null": null, "int": 0, "float": 3.14}}'
object_nested_node_json = '{"object": {"object": {"object": {}}}}'
consistent_list_root_node_json = '[{"key-0": ""}, {"key-0": ""}]'
consistent_list_nested_node_json = '{"list": [{"key-0": ""}, {"key-0": ""}]}'
inconsistent_list_root_node_json = '[{"key-0": ""}, {"key-1": ""}]'
inconsistent_list_nested_node_json = '{"list": [{"key-0": ""}, {"key-1": ""}]}'

# Outputs
jtv_help = '''\

   {●}
    ║SON
    ╠══╦══
  ══╝  ║
       ║REE VIEWER          v-VERSION

  Description:
    jtv, a command line utility for visualising JSON and YAML schemas as text trees

  Synopsis:
    jtv -h|-j|-y [--mode first|union|distinct]

  Flags:
    -h: Show this message
    -j: Read JSON from stream
    -y: Read YAML from stream

  Options:
    --mode first|union|distinct: Array evaluation mode.

  Examples:
    Read JSON from stream:
    $ echo \'{"0": {"00": [{"000": "", "001": true, "002": []}]}, "1": {"10": []}}\' | jtv -j

    Read YAML from stream:
    $ cat file.yml | jtv -y

  Legend:
    {object_node}
    [array_node] 
    "string_node"
    boolean_node 
    null_node    
    int_node     
    float_node   

'''.replace('VERSION', __version__)

jtv_valid_yaml = '''\

{●}
 └── {root_node}
     ├── "name"
     ├── {nested_node}
     │   └── "name"
     └── [array]

'''

jtv_object_empty_root_node = '''\

{●}

'''

jtv_object_empty_nested_node = '''\

{●}
 └── {object}

'''

jtv_object_nested_node = '''\

{●}
 └── {object}
     └── {object}
         └── {object}

'''

jtv_list_empty_root_node = '''\

[●]

'''

jtv_list_empty_nested_node = '''\

{●}
 └── [list]

'''

jtv_string_empty_node = '''\

{●}
 └── "string"

'''

jtv_object_node_and_types = '''\

{●}
 └── {object}
     ├── [array]
     ├── "string"
     ├── boolean
     ├── null
     ├── int
     └── float

'''

jtv_mode_distinct_for_consistent_root_node = '''\

[●]
 └── "key-0"

'''

jtv_mode_first_for_consistent_root_node = '''\

[●]
 └── "key-0"

'''

jtv_mode_union_for_consistent_root_node = '''\

[●]
 └── "key-0"

'''

jtv_mode_distinct_for_consistent_nested_node = '''\

{●}
 └── [list]
     └── "key-0"

'''

jtv_mode_first_for_consistent_nested_node = '''\

{●}
 └── [list]
     └── "key-0"

'''

jtv_mode_union_for_consistent_nested_node = '''\

{●}
 └── [list]
     └── "key-0"

'''

jtv_mode_distinct_for_inconsistent_root_node = '''\

[●]
 ├── {◎-schema-0}
 │   └── "key-0"
 └── {◎-schema-1}
     └── "key-1"

'''

jtv_mode_first_for_inconsistent_root_node = '''\

[●]
 └── "key-0"

'''

jtv_mode_distinct_for_inconsistent_nested_node = '''\

{●}
 └── [list]
     ├── {◎-schema-0}
     │   └── "key-0"
     └── {◎-schema-1}
         └── "key-1"

'''

jtv_mode_first_for_inconsistent_nested_node = '''\

{●}
 └── [list]
     └── "key-0"

'''

jtv_mode_union_for_inconsistent_root_node = '''\

[●]
 ├── "key-0"
 └── "key-1"

'''

jtv_mode_union_for_inconsistent_nested_node = '''\

{●}
 └── [list]
     ├── "key-0"
     └── "key-1"

'''

jtv_invalid_json = '''\
Error: expecting JSON format.

'''

jtv_invalid_yaml = '''\
Error: expecting YAML format.

'''