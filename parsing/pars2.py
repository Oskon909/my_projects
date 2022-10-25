# write parser for https://salexy.kg/  all category

def get_category(POSTSOUD):
    perl = POSTSOUD.find(class_='breadcrumb').find_all('span')
    return perl[1].text

