__author__ = 'Chetan'
import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import sqlite3

def _execute(query):
    """ Method to run query on sqlite db """
    dbPath = 'db'
    connection = sqlite3.connect(dbPath)
    cursorobj = connection.cursor()
    try:
        cursorobj.execute(query)
        result = cursorobj.fetchall()
        connection.commit()
    except Exception:
            raise
    connection.close()
    return result

class IndexHandler(tornado.web.RequestHandler):
    """ Home Page """
    def get(self):
        query = "select * from task"
        todos = _execute(query)
        self.render('index.html', todos=todos)

class NewHandler(tornado.web.RequestHandler):
    """ Add a task to teh task list """
    def post(self):
        name = self.get_argument('name', None)
        query = "create table if not exists task (id INTEGER PRIMARY KEY, name TEXT, status NUMERIC) "
        _execute(query)
        query = "insert into task (name, status) values ('%s', %d) " %(name, 1)
        _execute(query)
        self.redirect('/')

    def get(self):
        self.render('new.html')

class UpdateHandler(tornado.web.RequestHandler):
    """ Update status of the task to Open/Closed"""
    def get(self, id, status):
        query = "update task set status=%d where id=%s" %(int(status), id)
        _execute(query)
        self.redirect('/')

class DeleteHandler(tornado.web.RequestHandler):
    """ Delete task from task list """
    def get(self, id):
        query = "delete from task where id=%s" % id
        _execute(query)
        self.redirect('/')

class RunApp(tornado.web.Application):
    """ Configuration to run the App """
    def __init__(self):
        Handlers = [
            (r'/', IndexHandler),
            (r'/todo/new', NewHandler),
            (r'/todo/update/(\d+)/status/(\d+)', UpdateHandler),
            (r'/todo/delete/(\d+)', DeleteHandler),
        ]
        settings = dict(
            debug=True,
            template_path='templates',
            static_path="static",
        )
        tornado.web.Application.__init__(self, Handlers, **settings)

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(RunApp())
    http_server.listen(5000)
    tornado.ioloop.IOLoop.instance().start()