# användare som har ett namn i form av nyckel i en dict
# lista med intressen som värde 

# gå genom varje nyckel och dess intressen 
# jämföra om dom finns i använarens lista med intressen
# för varje matchning +1 i "matchningsvärde"
# skapa en ny lista med listor som innehåller nyckeln samt "matchningsvärdet"
# titta vilken nyckel som har högst matchningsvärde och lägg den först i en variabel 


# intressen som finns inlagda: 
# hästar, sport, träning, historia, mat, läsa, golf, promenader
users = {"pelle": ["hästar", "sport", "träning", "historia"], "adam": ["mat", "läsa"], "karin": ["golf", "promenader", "mat"]}
my_interests = []
running = True
while running:
    input_interest = input("Skriv ett intresse: ")
    my_interests.append(input_interest)
    if input_interest == "exit":
        running = False
match_value = 0
matched_dict = {}

#print(users["pelle"])

for key in users:
    match_value = 0
    print("user:", key)
    #print("interests:")
    #print(users[key])
    for io in users[key]:
        for im in my_interests:
            if io == im:
                print("MATCH")
                match_value += 1
    matched_dict[key] = match_value


            #print(io)
print(matched_dict)    
# print(match_value)
# print("MY INTERESTS:")
# for i in my_interests:
#     print(i)
    
#     #if i in 


    



# e_dict = {1: "one", 2: "two", 3: "three"}
# print(1 in e_dict)
# print(e_dict[1])
# print("two" in e_dict.values())
# print(e_dict.keys())
# print(e_dict.values())