# lab2
def filter(people):
	filtred =[]
	for p in people:
		for child in p.get("children"):
			if child["age"]>=18:
				filtred.append(p)
	return filtred
	
ivan ={
	"name": "ivan",
	"age": 34,
	"children":[{
		"name":"vasja",
		"age":12,
	},
	{
		"name":"petya",
		"age":10,
	}],
	
}
darja={
	"name":"darja",
	"age":41,
	"children":[{
		"name":"kirill",
		"age":21,
},{
		"name":"pavel",
		"age":15,
}],
}
emps = [darja, ivan]
filtred_people= filter(emps)
for p in filtred_people:
	print(p["name"])


	
