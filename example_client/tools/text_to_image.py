from gladier import GladierBaseTool, generate_flow_definition


def simple_image_function(**data):
    import os
    wfile = data['file']
    text = data['text']

    if '~' in wfile:
        wfile = os.path.expanduser(wfile)

    with open(wfile,"w") as file1:
        file1.writelines(text)

    return wfile

@generate_flow_definition
class SimpleImageTool(GladierBaseTool):
    funcx_functions = [simple_image_function]
    required_input = [
        'file',
        'text', 
        'funcx_endpoint_compute'
        ]
