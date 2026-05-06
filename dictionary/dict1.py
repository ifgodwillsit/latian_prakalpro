#mencari bilangan berapa aja di antara range a dan b yang punya faktor sebesar(< > <= >= ==) bilangan value
# from preloaded import A001055 # to remember you the name of the database
import operator

def inf_database(range_, str_, val):
    ops = {"higher than": operator.gt, "lower than": operator.lt, "equals to": operator.eq, "higher and equals to": operator.ge, "lower and equals to": operator.le} 
    if str_ not in ops:
        return "wrong constraint"
    
    result = [i for i in range(range_[0], range_[-1] + 1) if ops[str_](A001055[i], val)]
    return (len(result), result)