import urllib.request
import  re
import  string
def iwant():

        with open("finding.txt",'r') as f:
            line = f.readline()
            with open("finished.txt",'r') as f1:
                finishString=f1.read()
                if(finishString!=""):
                    print("检测到进度："+finishString)
                    while(finishString.strip()!=line.strip()):
                        line=f.readline()
                else:
                    print("没有进度")
                f1.close()
                while(line):
                    isAvailable(line.strip())
                    save(line.strip(),"finished.txt",'w')
                    line = f.readline()

        f.close()






def isAvailable(str):
    try:
        response = urllib.request.urlopen("http://panda.www.net.cn/cgi-bin/check.cgi?area_domain="+str+".com")
    except urllib2.URLError:
        print("请求："+str+"时发生异常")
        return
    strResponse=response.read().decode('utf-8')
    result=re.findall(r"Domain name is (available)",strResponse,)
    save(str,"finished.txt",'w')
    if result!=[]:
         save(str+":可用\n","available.txt",'a')

def save(content,filename,way):
    f=open(filename,way)
    f.write(content)
    f.close()


iwant()
#
# for i in string.ascii_lowercase:
#     for j in string.ascii_lowercase:
#         for k in string.ascii_lowercase:
#             for l in string.ascii_lowercase:
#                 string1=i+j+k+l
#                 f = open("finding.txt", 'a')
#                 f.write(string1+"\n")
#                 f.close()
