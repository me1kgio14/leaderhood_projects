def human_years_cat_years_dog_years(human_years):
    cat=0
    dog=0
    if human_years==1:
        cat+=15
        dog+=15
    elif human_years==2:
        cat+=24
        dog+=24
    elif human_years>=3:
        cat=cat+(24+(human_years-2)*4)
        dog=dog+(24+(human_years-2)*5)
    year=[]
    year.append(human_years) 
    year.append(cat) 
    year.append(dog) 
    return year