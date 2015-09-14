html_template = \
"""
<html>
<head>
<title> job search </title>
</head>
# for (i) in (list) #
<p><a href = (i.url) > (i.content) </a></p>
# endfor #
</html>
"""

def template(html_list, url_list, start_index, end_index):
    perv_string = "\n".join(html_list[:start_index])
    next_string = "\n".join(html_list[end_index + 1:])
    template_string = '\n'.join(html_list[start_index+1:end_index])
    template_list = template_string.split(' ')
    index_i = template_list.index("(i.url)")
    index_content = template_list.index("(i.content)")
    string = ""
    for url in url_list:
        _template_list = template_list[:]
        _template_list[index_i] = url[0]
        _template_list[index_content] = url[1]
        string += " ".join(_template_list)
        string += "\n"
    string = perv_string +"\n"+ string +"\n"+ next_string
    print string
    return string
result_list = [["www.baidu.com", "haha"],["www.google.com", "haha"]]
html_list = html_template.split('\n')
start_index = 0
end_index = 0
for i in range(len(html_list)):
    if "for" in html_list[i] and "in" in html_list[i]:
        start_index = i
    elif "endfor" in html_list[i]:
        end_index = i
url_list = [
    ['http://job.cqupt.edu.cn/#rec:739', "1"],
    ['http://job.cqupt.edu.cn/#rec:677', "2"]

]
html_template = template(html_list, url_list, start_index, end_index)

fp = open("h.html", "wb")
fp.write(html_template)
fp.close()
