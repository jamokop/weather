import tornado.ioloop
import tornado.web
from tornado.httpclient import AsyncHTTPClient
from datetime import datetime
import urllib

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        url = 'http://127.0.0.1:5001/weather'
        city,start,end = self.validate()
        query_string = {'city':city}
        if start and end:
            query_string['start'] = start
            query_string['end'] = end

        url = url+'?'+urllib.parse.urlencode(query_string)
        print(url)
        http_client  = AsyncHTTPClient()
        try:
            response = await http_client.fetch(url)
        except Exception as e:
            self.write("Error: %s" % e)
        else:
            json = tornado.escape.json_decode(response.body)
            self.write(json)


    def validate(self):
        dateformat = "%Y-%m-%d %H:%M:%S"
        city = self.get_query_arguments(name = 'city')
        if not city:
            return self.finish({
                'query arguments' : {
                    'city' : {
                        'required':'required',
                        'format':'string'
                    },
                    'start' : {
                        'required':'optional',
                        'format': 'datetime (Y-m-d H:i:s)'
                    },
                    'end' : {
                        'required':'optional',
                        'format': 'datetime (Y-m-d H:i:s)'
                    }
                }
            })

        start = self.get_query_arguments(name='start')
        end =  self.get_query_arguments(name='end')

        if (start and not end) or (end and not start):
            return self.finish({
                'error' : 'please provide date in a range'
            })

        if start and end:
            try:
                start = start[0]
                end = end[0]
                date1 = datetime.strptime(start, dateformat)
                date2 = datetime.strptime(end, dateformat)
                if date1 > date2:
                    start,end = end,start
            except ValueError:
                return self.finish({'error':'Incorrect data format, should be Y-m-d H:i:s'})

        return city[0],start,end

def make_app():
    return tornado.web.Application([
        (r"/api/v1/weather", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
