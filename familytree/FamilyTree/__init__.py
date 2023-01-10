class Member():
    def __init__(self, name, father, mother):
        self.name = name
        self.father = father
        self.mother = mother
        self.children = []


family = {}


def add_member(name, father, mother):  # 添加成员
    if name:
        member = Member(name, father, mother)
        family[name] = member
        if father in family:
            family[father].children.append(member)
        if mother in family:
            family[mother].children.append(member)
        return True
    else:
        return False


def get_ancestors(name):  # 找出所有父辈
    if name not in family:
        return print('查无此人')
    parents = []
    member = family[name]
    while member.father in family or member.mother in family:
        if member.father in family:
            parents.append(member.father)
            member = family[member.father]
        elif member.mother in family:
            parents.append(member.mother)
            member = family[member.mother]
    return parents


def get_brother(name):  # 找兄弟
    if name not in family:
        return print('查无此人')
    brothers = []
    member = family[name]
    if member.father in family:
        brothers.extend(family[member.father].children)
    if member.mother in family:
        brothers.extend(family[member.mother].children)
    brothers = [brother.name for brother in brothers if brother.name != name]
    return brothers


def get_children(name):  # 找出孩子
    if name not in family:
        return print('查无此人')
    member = family[name]
    return [child.name for child in member.children]


def getFather(name):
    if family[name].father:
        return family[name].father
    else:
        return 'None'


def getMother(name):
    if family[name].mother:
        return family[name].mother
    else:
        return 'None'


def remove(name):  # 移除成员
    if name in family:
        family.pop(name)
        # 删除时注意节点


def getMessage(name):
    if name in family:
        children = str(get_children(name))
        children = removeBraces(children)
        return "父亲: " + getFather(name) + "\n" + "母亲: " + getMother(name) + "\n" + "孩子: " + children
    else:
        return "查无此人"


def removeBraces(text):
    text = text.replace("[", " ")
    text = text.replace("'", "")
    text = text.replace(" ", "")
    text = text.replace("]", " ")
    return text


def getGenology(name):
    if name not in family:
        return "查无此人"
    if name in family:
        if not get_ancestors(name):
            return getGeneration(name, 1)
        else:
            a = get_ancestors(name)
            b = a[-1]
            return getGeneration(b, 1)


def getGeneration(name, level):
    output = ''
    if name not in family:
        return '查无此人'
    for i in range(0, level):
        output = output + '--'
    output = output + name + '\n'
    children = get_children(name)
    l = len(children)
    for i in range(0, l):
        childName = children[i]
        output = output + getGeneration(childName, level + 1)
    return output


def loadDefaultData():
    add_member('爷爷', None, None)
    add_member('奶奶', None, None)

    add_member('爸', '爷爷', '奶奶')
    add_member('大姑', '爷爷', '奶奶')
    add_member('小姑', '爷爷', '奶奶')
    add_member('妈', None, None)

    add_member('我', '爸', '妈')
    add_member('儿子', '我', '老婆')
    add_member('老婆', None, None)

    add_member('孙子', '儿子', '儿子老婆')

    add_member('曾孙', '孙子', None)
    add_member('小哥', '小姑', None)


if __name__ == '__main__':
    # 插入顺序要根据辈分依次插入
    loadDefaultData()

    print(getGenology('我'))
    print(getMessage('爷爷'))
