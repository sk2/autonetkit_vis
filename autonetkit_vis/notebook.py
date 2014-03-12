from IPython.display import HTML
import autonetkit.config as config
host = config.settings['Http Post']['server']
port = config.settings['Http Post']['port']
http_url = "http://%s:%s" % (host, port)

def display(width = 700, height = 350):
    html = ('<iframe src=%s width=%s height=%s></iframe>' % (http_url, width, height))
    return html
    HTML(html)

def display3d(width = 700, height = 350):
    html = ('<iframe src=%s/3d/html width=%s height=%s></iframe>' % (http_url, width, height))
    HTML(html)


def save(filename, overlay_id = "phy", extension = "png"):
    from selenium import webdriver
    driver = webdriver.PhantomJS() # or add to your PATH
    driver.set_window_size(1024, 768) # optional
    driver.get('%s/simple.html?overlay=%s' % (http_url, overlay_id))
    driver.save_screenshot('%s.%s' % (filename, extension)) # save a screenshot to disk
    driver.close()


    #TODO: make a class: mosto fh time is setting up phantomjs - but check memory usage
def screenshot(overlay_id = "phy", width=800, height = 600):
    try:
        from selenium import webdriver
        driver = webdriver.PhantomJS() # or add to your PATH
        driver.set_window_size(width, height) # optioffonal
        driver.get('%s/simple.html?overlay=%s' % (http_url, overlay_id))
        result = driver.get_screenshot_as_png()
        driver.close()
        return result
    except Exception, e:
        #TODO: check how this works with image
        print "Unable to create screenshot: %s" % e

def svg(overlay_id = "phy", width=800, height = 600):
    try:
        from selenium import webdriver
        driver = webdriver.PhantomJS() # or add to your PATH
        driver.set_window_size(width, height) # optioffonal
        driver.get('%s/simple.html?overlay=%s' % (http_url, overlay_id))
        js = '''return document.getElementsByClassName("visualisation")[0].innerHTML'''
        result = driver.execute_script(js)
        driver.close()
        return result
    except Exception, e:
        #TODO: check how this works with image
        print "Unable to create screenshot: %s" % e


document.getElementsByClassName("f-svg f-topology-bg")[0]