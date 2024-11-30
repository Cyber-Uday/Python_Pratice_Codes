
#here we are going to match the status with our web url and be procees with switch case..!

def https_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "DATA NOT FOUND"
        case default:
            return "THIS IS DEFAULT>> "
        
print(https_status(404))