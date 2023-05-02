import json
import re
from collections import OrderedDict

from markdown_to_json.markdown_to_json import CMarkASTNester, Renderer
from markdown_to_json.vendor import CommonMark

README_FILENAME = "README.md"
CONTENT_START_TAG = "<!--CONTENT-->"
CONTENT_STOP_TAG = "<!--CONTENT-->"


def extract_unsorted_markdown_content(filename, content_start_tag, content_stop_tag):
    """Extracts from README file the markdown content to be sorted"""
    with open(filename, "r") as f:
        # The content to be sorted is between two specific tags
        markdown_content = re.search(
            f"{content_start_tag}(.*?){content_stop_tag}", f.read(), re.DOTALL
        ).group(1)
    # A level-one markdown heading must be added to allow correct sorting
    return "# Content\n" + markdown_content


def convert_markdown_to_json(markdown_content):
    """Convert the markdown content to a JSON object (OrderedDict)"""
    nester = CMarkASTNester()
    renderer = Renderer()
    ast = CommonMark.DocParser().parse(markdown_content)
    nested = nester.nest(ast)
    rendered = renderer.stringify_dict(nested)
    return rendered


def sort_json(json):
    """Recursively sorts a JSON object (OrderedDict)"""
    res = OrderedDict()
    for k, v in sorted(json.items()):
        if isinstance(v, dict):
            res[k] = sort_json(v)
        elif isinstance(v, list):
            res[k] = sorted(v)
        else:
            res[k] = v
    return res


def to_markdown(json, markdown_content, level=1):
    """Recursively converts a JSON object to markdown"""
    if isinstance(json, dict):
        for k, v in json.items():
            if level > 1:
                markdown_content.append("")
                markdown_content.append("#" * level + " " + k)
            to_markdown(v, markdown_content, level=level + 1)
    elif isinstance(json, list):
        for v in json:
            to_markdown(v, markdown_content, level=level + 1)
    else:
        markdown_content.append("- " + json)


def convert_json_to_markdown(json):
    """Converts the JSON object to markdown"""
    markdown_content = []
    to_markdown(json, markdown_content)
    return "\n".join(markdown_content)


def replace_sorted_markdown(
    filename, content_start_tag, content_stop_tag, markdown_content
):
    """Replaces sorted markdown content in README file"""
    # Open the file for reading
    with open(filename, "r") as f:
        # Read the contents of the file
        file_contents = f.read()

    # # Use regular expressions to find the text between the tags
    # pattern = re.compile(
    #     f"(?<={content_start_tag}).*?(?={content_stop_tag})", re.DOTALL
    # )
    # old_text = re.search(pattern, file_contents).group(0)

    # Replace the old text with the new text
    file_contents = re.sub(
        f"{content_start_tag}.*?{content_stop_tag}",
        f"{content_start_tag}\n{markdown_content}\n{content_stop_tag}",
        file_contents,
        flags=re.DOTALL,
    )

    # Open the file for writing and write the modified contents
    with open(filename, "w") as f:
        f.write(file_contents)


def main():
    """Main method"""
    # Extract unsorted content from the README file
    unsorted_markdown_content = extract_unsorted_markdown_content(
        filename=README_FILENAME,
        content_start_tag=CONTENT_START_TAG,
        content_stop_tag=CONTENT_STOP_TAG,
    )

    # Convert unsorted markdown content to JSON object
    json_content = convert_markdown_to_json(markdown_content=unsorted_markdown_content)

    # Print unsorted JSON object
    # print(json.dumps(json_content, indent=2))

    # Sort JSON object
    sorted_json_content = sort_json(json=json_content)

    # Print sorted JSON object
    # print(json.dumps(sorted_json_content, indent=2))

    # Convert sorted JSON object to markdown content
    sorted_markdown_content = convert_json_to_markdown(json=sorted_json_content)

    # Print sorted markdown content
    # print(sorted_markdown_content)

    # Replace sorted markdown content in the README file
    replace_sorted_markdown(
        filename=README_FILENAME,
        content_start_tag=CONTENT_START_TAG,
        content_stop_tag=CONTENT_STOP_TAG,
        markdown_content=sorted_markdown_content,
    )


if __name__ == "__main__":
    main()
