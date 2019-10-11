import urllib.request
import socket


def test(url, timeout=5):
    # we define a request object that is equal to requests
    url = url.rstrip('\n')
    address = "http://"+url
    # trying with http
    try:
        status = urllib.request.urlopen(address, timeout=timeout).getcode()
        return status
    except urllib.request.URLError as e:
        # trying with https
        address1 = "https://"+url
        try:
            status = urllib.request.urlopen(address1, timeout=timeout).getcode()
            return status
        except urllib.request.URLError as e:
            # trying with https with port number
            address2 = "https://" + url + ":443"
            try:
                status = urllib.request.urlopen(address2, timeout=timeout).getcode()
                return status
            except urllib.request.URLError as e:
                # trying with http and port number
                address3 = "http://"+url+":80"
                try:
                    status = urllib.request.urlopen(address3, timeout=timeout).getcode()
                    return status
                except urllib.request.URLError as e:
                    x = "Not Reachable"
                    return x
                except socket.timeout as e:
                    y = "Connection Timeout"
                    return y
            except socket.timeout as e:
                y = "Connection Timeout"
                return y
        except socket.timeout as e:
            y = "Connection Timeout"
            return y
    except socket.timeout as e:
        y = "Connection Timeout"
        return y
