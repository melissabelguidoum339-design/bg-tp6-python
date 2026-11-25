 
import json

(
def B(moyenne: float) -> bool:
     
    if moyenne >= 10:
        return True
    else:
        return False


def A(students: list) -> str:
     
    resultats = []
    
    
    for etudiant in students:
        
        matricule = etudiant[0]
        moyenne = etudiant[3]
        
        
        if B(moyenne):
            statut = "ADMIS"
        else:
            statut = "AJOURNE"
            
         (Slide 27, 31 & 32)
        resultats.append({
            "mat": matricule,
            "result": statut
        })
        
     
    return json.dumps(resultats)


def C(students: list):
    
    res_json = A(students)
    
    res_list = json.loads(res_json)
    
    
    for item in res_list:
        
        print(f"{item['mat']} : {item['result']}")


if __name__ == "__main__":
     
    students = [
        (1000, "JOHN", "DOE", 14, 5),
        (2000, "BOB", "CARLTON", 7, 1),
        (3000, "RAYANE", "SMITH", 13, 3)
    ]
    
     
    C(students)
