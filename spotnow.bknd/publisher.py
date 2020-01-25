#  MIT License
# Copyright (c) 2018 KubeMQ
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE. 


import datetime

from kubemq.events.lowlevel.event import Event
from kubemq.events.lowlevel.sender import Sender

def createEvent(b,cid):
    return Event(
            metadata="EventMetaData",
            body=b.encode('UTF-8'),
            store=False,
            channel="smartlock",
            client_id=cid
    )

if __name__ == "__main__":

    publisher  = Sender("51.105.156.152:50000")
    '''
    eventopen = Event(
        metadata="EventMetaData",
        body =("OPEN").encode('UTF-8'),
        store=False,
        channel="smartlock",
        client_id="1"
    )
    '''
    #Client ID default = 0
    clientID = 0
    while True:
        try:
            action = input("""Insert 1 to change Client ID\n
                            Insert 2 to show Client ID\n
                            Insert 3 to open garage\n
                            Insert 4 to close garage\n
                            Insert 5 to exit\n 
                            """)
            # Change client ID
            if action == 1:
                clientID = input("Insert client id.")
            # Show current client ID
            if action == 2:
                print(clientID)
            # Open garage
            if action == 3:
                body = "OPEN"
                event = createEvent(body,clientID)
                res = publisher.send_event(event)
                print(res)
            # Close garage
            if action == 4:
                body = "CLOSE"
                event = createEvent(body,clientID)
                res = publisher.send_event(event)
                print(res)
            # Shutdown
            if action == 5:
                break

        except Exception as err:
            print(
                "'error sending:'%s'" % (
                   err
                )
            )

