def fun(s):
    # return True if s is a valid email, else return False
    if s.count("@") == 1 and s.count(".") == 1:
        # i = s.index("@")
        uname, webex = s.split('@')
        web, ext = webex.split('.')
        if uname.replace('-', '').replace('_', '').isalnum() is False:
            return False
        elif web.isalnum() is False:
            return False
        elif ext.isalpha() is False or len(ext) > 3:
            return False
        else:
            return True
    else:
        return False
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    # n = int(input())
    
    emails = ["its@gmail.com1" , "mike13445@yahoomail9.server" , "rase23@ha_ch.com" , "daniyal@gmail.coma" , "thatisit@thatisit"]
    # for _ in range(n):
    #     emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)