files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']

# 내 코드
print(list(filter(lambda x: x[-3:] == 'jpg' or x[-3:] == 'png', files)))
# 코딩 도장 코드
print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))