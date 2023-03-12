"""
First pass at converting old to new format.

This will not get callout or exercises.
"""

import sys
import re

from string import Template

overview = Template("""````{admonition} Overview
:class: overview

Questions:
$questions

Objectives:
$objectives
````
""")

keypoints = Template("""````{admonition} Key Points
:class: key

$key_points
````
""")
                     
new_block = Template("""````{tab-set-code} 

```{code-block} $language
$code
```
````
""")
                     

if __name__ == "__main__":
    filename = sys.argv[1]

    with open(filename) as f:
        text = f.read()

    overview_re = """(---
(.+)
---)
"""

    pat = re.compile(overview_re, re.DOTALL)
    results = pat.findall(text)

    section_text = results[0][1].replace('"', '')

    title_pat = "title: (.+)"
    section_pat = re.compile(title_pat)
    title = section_pat.findall(section_text)[0]

    bullets = """([A-Za-z]+):\n(.*(?:\n- .*)*)"""
    section_pat = re.compile(bullets)
    res = section_pat.findall(section_text)


    section_dict = {x[0]: x[1] for x in res}

    overview_text = overview.substitute(questions = section_dict["questions"], objectives=section_dict["objectives"])

    text = f"# {title}\n\n" + text
    text = text.replace(results[0][0], overview_text)

    old_block = """(~~~
(.+?)
~~~
{: .(.+?)})
"""

    pat = re.compile(old_block, re.DOTALL)

    results = pat.findall(text)

    for result in results:
    
        if "language" in result[2]:
            language = result[2].split("-")[1]
        else:
            language = result[2]
        
        if language == "bash":
            language = "shell"

        code = result[1]

        if language == "shell":
            code.replace("$", "")
        
        new_string = new_block.substitute(language=language, code=code)

        text = text.replace(result[0], new_string)

    text += keypoints.substitute(key_points=section_dict["keypoints"])


    with open("out.txt", "w+") as f:
        f.write(text)





