import requests
import time
import queue
import argparse
import threading


class Scan(object):

    def __init__(self, url, inputDict, output, threadNum):
        print("[*] Scanning is starting...")
        self.url = url if url.find("://") != -1 else "http://"+url
        print("[+] Scan target url:", self.url)
        self.inputDict = inputDict
        self.oFileName = output+".txt" 
        createFile = open(self.oFileName,"w")
        createFile.close()
        self.threadNum = threadNum
        self.lock = threading.RLock()
        self._analysis404()
        self._loadHeaders()
        self._loadDict(self.inputDict)
        self.STOP = 0

    def _loadHeaders(self):
        self.headers = {
            'Accept': '*/*',
            'Referer': 'http://www.baidu.com',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; ',
            'Cache-Control': 'no-cache',
        }
    def _analysis404(self):
        notFoundPage = requests.get(self.url + '/songgeshigedashuaibi/hello.html', allow_redirects=False)
        self.notFoundPageText = notFoundPage.text.replace('/songgeshigedashuaibi/hello.html', '')

    
    def _loadDict(self,inputDict):
        self.q = queue.Queue()
        with open(inputDict,"r+",encoding="utf-8") as f:
            for line in f:
                self.q.put(line.strip("\n"))
        if self.q.qsize() < 0:
            print("[*] The dictionary is Null. Please check....") 
            exit()
    
    
    def _writeReult(self, result):
        self.lock.acquire()
        with open(self.oFileName, "a+") as f:
            f.write(result + "\n")
        self.lock.release()
    
    def _scan(self, url):
        html_result = 0
        try:
            html_result = requests.get(url, allow_redirects=False, timeout=60)
           
        except requests.exceptions.ConnectionError:
            # print 'Request Timeout:%s' % url
            pass
        finally:
            if html_result != 0:
                if html_result.status_code == 200: #and html_result.text != self.notFoundPageText:
                    print("The current theading is %s" % threading.currentThread().name, end = "")
                    print('\t[%i]%s' % (html_result.status_code, html_result.url))
                   
                    self._writeReult('[%i]%s' % (html_result.status_code, html_result.url))

    def run(self):
        while not self.q.empty() and self.STOP == 0:
            url = self.url + self.q.get()
            self._scan(url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url",   help = "the url you want to scan", type=str)
    parser.add_argument("-t", "--threadNum", dest="threadNum", help = "The number of thread you scanning.", type = int, default = 60)
    parser.add_argument("-i", "--input", dest="inputDict", help = "The input about dictionary", type=str,default = "dict1.txt")
    parser.add_argument("-o", "--output",dest="output", help="the file of output", type=str, default="result")
    
    args = parser.parse_args()
    scan = Scan(args.url, args.inputDict, args.output, args.threadNum)
    start = time.time()
    print("[*] Start time:",start)
   
    for i in range(args.threadNum):
        t = threading.Thread(target=scan.run, daemon=True)
        #t.setDaemon(True)
        t.start()
    while True:
        if threading.activeCount() <= 1:
            break
        else:
            try:
                time.sleep(0.1)
            except KeyboardInterrupt:
                print('\n[WARNING] User aborted, wait all slave threads to exit, current(%i)' % threading.activeCount())
                scan.STOP = 1
    
    end = time.time()

    print('Scan end!!!Total time:',end-start)
    