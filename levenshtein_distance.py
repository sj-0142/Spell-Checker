
dictionary = [ "Doctor",
 "Lawyer",
 "Teacher",
 "Engineer",
 "Accountant",
 "Nurse",
 "Police",
 "Architect",
 "Dentist",
 "Pharmacist"]



def iterative_lev_dist(s,t):

    rows = len(s)+1
    cols = len(t)+1
    dist = [[0 for x in range (cols)]for x in range (rows)]


    for i in  range (1,rows):
        dist[i][0] = i
    
    for i in range (1,cols):
        dist[0][i] = i
    
    for col in range(1,cols):
        for row in range(1,rows):
            if s[row-1]==t[col-1]:
                cost = 0
            else:
                cost = 1
            
            dist[row][col] = min(dist[row-1][col]+1,
                                 dist[row][col-1]+1,
                                 dist[row-1][col-1]+cost)
    return dist[row][col]



def correct_spelling(input_str):
    min_score_index = 1000
    ans=""
    for word in dictionary:
        temp = iterative_lev_dist(word, input_str.lower())
        if temp<min_score_index:
            ans = word
            min_score_index = temp

    return ans
a = "Llwayrer"
print(f'The correct spelling of {a} is: {correct_spelling(a)}')







        
    



