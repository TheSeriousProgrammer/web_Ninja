import wikipedia

def search_query(word):
    matches=wikipedia.search(word)
    if matches==[]:
        print("I understood your question yet i don't know the answer!!")
    else:
        print()
        print('Which one of these ?')
        print()
        if len(matches)<10:
            for i in range(len(matches)):
                print(i+1,')',matches[i])
        else:
            for i in range(10):
                print(i+1,')',matches[i])
    option=int(input("Enter the serial number of your choice:"))-1
    print()
    print("Results from wikipedia:" + '\n\n' + wikipedia.summary(matches[option%10],sentences=5))
    print()

while True :
    print()
    query=input("Query :").strip().lower()
    if query=='bye':
        print("Thank you")
        break
    elif 'is' in query :
        seperator=query.find('is')
        #print('Its happening')
        search_content=query[seperator+2:]
        #print('Its happening')
        search_query(search_content)
    elif 'are' in query :
        seperator=query.find('are')
        search_content=query[seperator+3:]
        search_query(search_content)
    else:
        print("Sorry I don't get the question")
