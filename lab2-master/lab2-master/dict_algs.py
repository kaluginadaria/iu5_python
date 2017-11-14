def filter(people):
    filtred = []
    for p in people:
        for child in p.get("children"):
            if p in filtred:
                break
            if child["age"] >= 18:
                filtred.append(p)
    return filtred


ivan = {
    "name": "ivan",
    "age": 34,
    "children": [{
        "name": "vasja",
        "age": 19,
    },
        {
            "name": "petya",
            "age": 21,
        }],

}
darja = {
    "name": "darja",
    "age": 41,
    "children": [{
        "name": "kirill",
        "age": 21,
    }, {
        "name": "pavel",
        "age": 22,
    }],
}
emps = [darja, ivan]
filtred_people = filter(emps)
for p in filtred_people:
    print(p["name"])