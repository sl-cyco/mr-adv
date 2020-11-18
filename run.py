# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'IyEvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvdXNyL2Jpbi9weXRob24zCiMgLSotIGNvZGluZzogdXRmLTggLSotCmZyb20gb3MgaW1wb3J0IHN5c3RlbSBhcyBzaGVsbCxsaXN0ZGlyLG1rZGlyLGNoZGlyLGdldGN3ZApmcm9tIG9zLnBhdGggaW1wb3J0IGV4aXN0cwpmcm9tIHN1YnByb2Nlc3MgaW1wb3J0IGdldG91dHB1dCBhcyBnZXQKZnJvbSByYW5kb20gaW1wb3J0IHJhbmRpbnQKZnJvbSBzaHV0aWwgaW1wb3J0IGNvcHlmaWxlLHJtdHJlZQpmcm9tIHN5cyBpbXBvcnQgZXhpdCBhcyBwcm50X2V4dAoKaWYgZXhpc3RzKCJhZHZtciIpOgoJcHJudF9leHQoIlxuXG5cdFx0XDAzM1swOzMxOzQwbUZpcnN0bHkgaW5zdGFsbCB0b29sICBbIHNoIGluc3RhbGwuc2ggXVxuXG5cbiIpCgpkZWYgYmFubmVyKCk6CgluYW1lX2JhciA9ICIiIiAnCiMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMKCSAnIHwgbG9sY2F0CgkgIiIiCgoJbmFtZSA9ICIiIiAnCiAJX3wgICAgICBffCAgX3xffF98ICAgICAgICAgICAgICAgICAgICAgICAgX3wKIAlffF98ICBffF98ICBffCAgICBffCAgICAgICAgX3xffF98ICAgIF98X3xffCAgX3wgICAgICBffAogCV98ICBffCAgX3wgIF98X3xffCAgICAgICAgX3wgICAgX3wgIF98ICAgIF98ICBffCAgICAgIF98CiAJX3wgICAgICBffCAgX3wgICAgX3wgICAgICBffCAgICBffCAgX3wgICAgX3wgICAgX3wgIF98CiAJX3wgICAgICBffCAgX3wgICAgX3wgICAgICAgIF98X3xffCAgICBffF98X3wgICAgICBffAoJJyB8IGxvbGNhdCIiIgoKCXNoZWxsKCJlY2hvIituYW1lX2JhcikKCXNoZWxsKCJlY2hvIituYW1lKQoJcHJpbnQoIlwwMzNbMTszMDs0MG0gXHQgwqkgc2NyaXB0ICBieSAgY3ljbyAgICAgIFsg'
love = 'VTu0qUOmBv8iM2y0nUIvYzAioF9moP1wrJAiVPOqVvxXPKAbMJkfXPWyL2uiVvghLJ1yK2WupvxXPtbXp2uyoTjbVzAfMJSlVvxtBlOvLJ5hMKVbXDbXpUWcoaDbVyjjZmAoZQfvX3A0pvulLJ5xnJ50XQZlYQZ2XFxeVwf0ZT1poykhZFQvudjtVUW1ovOAHvNtVvxXpUWcoaDbVykhZvQvudjtVRSxMPOhMKptp2ygVPNvXDcjpzyhqPtvKT4mVBXTePNtHzIgo3MyVTRtp2ygVPNvXDcjpzyhqPtvKT40VBXTePNtIJ5coaA0LJkfVPOpovVcPtc3nTyfMFOHpaIyBtbXPKqbnJkyVSElqJH6PDbWPKElrGbXPDxWL2uinJAyVQ0tnJ50XTyhpUI0XPWpoyAyoTIwqTyiovNtBvNvXFxXPDxWLaWyLJfXPDyyrTAypUDtIzSfqJISpaWipwbXPDxWpUWcoaDbVyjjZmAoZQfmZGf0ZT0hYv5coaMuoTyxYv4hVPVcPtbWPtycMvOwnT9cL2HtCG0tZGbXPDymnTIfoPtvL2kyLKVvXFN7VTWuoz5ypvtcPtxWpUWcoaDbVykhKT4vXDbWPKOhqJ0tCFNkPtxWpTkcp3DtCFOoKDbWPKOhqJ1fnKA0VQ0tJ10XPDyzo3VtpT4tnJ4toTymqTEcpvtcBtbWPDycMvOjov5cp251oJIlnJZbXGbXPDxWPKOlnJ50XPWpZQZmJmN7VvgmqUVbpzShMTyhqPtmZvjmAvxcXlV7AQOgKT4vX3A0pvujoaIgXFfvVBXTePNtVvgjovxXPDxWPKOhqJ1fnKA0YzSjpTIhMPujoaIgXDbWPDxWpT51oFf9ZDbWPDxWpTkcp3DhLKOjMJ5xXUOhXDbWPJyzVT5iqPOjoTymqPN6PtxWPKOlnJ50XPWpoyjjZmAoZGfmZGf0ZT1GFH0toTymqPOcplOyoKO0rF4hEzylp3EfrFOuMTDtLFOmnJ0tKT4vXDbWPJIfp2H6PtxWPKqbnJkyVSElqJH6PtxWPDy0pax6PtxWPDxWp2kwqUExK3OhVQ0tnJ50XTyhpUI0XPWpoyAyoTIwqPOuVT51oJWypvOzo3VtpaIhVPN6VPVcXDbWPDxWPJyzVUAfL3E0MS9jovOho3DtnJ4tpT51oJkcp3D6PtxWPDxWPKOlnJ50XPWpZQZmJmN7ZmR7AQOgYv4hnJ52LJkcMPOm'
god = 'ZWxlY3Rpb24uLi4gIikKCQkJCQkJY29udGludWUKCQkJCQlicmVhawoJCQkJZXhjZXB0IFZhbHVlRXJyb3I6CgkJCQkJcHJpbnQoIlwwMzNbMDszMTs0MG0uLi5pbnZhbGlkLi4uICIpCgkJCQkKCQkJcGF0aCA9IHN0cihwbGlzdFtzbGN0dGRfcG4tMV0pCgkJCXNoZWxsKCJjZCAiK3BhdGgrIiA7IHB5dGhvbiBhZHZtci5weSIpCgkJYnJlYWsKCQoJaWYgY2hvaWNlID09IDI6CgkJc2hlbGwoImNsZWFyIikgOyBiYW5uZXIoKQoJCW1vYiA9IGludChpbnB1dCgiXDAzM1swOyIrc3RyKHJhbmRpbnQoMzIsMzYpKSsiOzQwbVxuXG5FbnRlciBkaWFsb2cgbnVtYmVyIFt0aGlzIGlzIG9ubHkgYWxpYXMgZm9yIHNpbSBsaXN0XSAgOiAiKSkKCQlta2RpcihzdHIobW9iKSkKCQljb3B5ZmlsZSgiYWR2bXIucHkiLHN0cihtb2IpKyIvYWR2bXIucHkiKQoJCWNoZGlyKHN0cihtb2IpKQoJCXVybCA9IGlucHV0KCJcblxuZW50ZXIgVXJsIDogIikKCQlhdXRoID0gaW5wdXQoIlxuZW50ZXIgQXV0aG9yaXphdGlvbiA6ICIpCgkJdXJsX2NvbnRlbnQgPSAgb3BlbigidXJsIiwidyIpCgkJYXV0aF9jb250ZW50ID0gb3BlbigiYXV0aCIsInciKQoJCXVybF9jb250ZW50LndyaXRlKHVybCkKCQlhdXRoX2NvbnRlbnQud3JpdGUoYXV0aCkKCQl1cmxfY29udGVudC5jbG9zZSgpCgkJYXV0aF9jb250ZW50LmNsb3NlKCkKCQlzaGVsbCgiY2xlYXIiKSA7IGJhbm5lcigpCgkKCQlpZiBleGlzdHMoImFkdm1yLnB5Iik6CgkJCXByaW50KCJcMDMzWzA7MzI7NDBtTmV3IHNpbSAiK3N0cihtb2IpKyIgYWRkZWQuLi4gIikKCQllbHNlOgoJCQlwcmludCgiXDAzM1swOzMxOzQwbS4uLnNvbXRoaW5nIHdyb25nLi4uICIpCgkJYnJlYWsKCQoJaWYgY2hvaWNlID09IDM6CgkJc2hlbGwoImNsZWFyIikgOyBiYW5uZXIoKQoJCXByaW50KCJcblxuIikKCQlwbnVt'
destiny = 'VQ0tZDbWPKOfnKA0VQ0tJ10XPDyjoaIgoTymqPN9VSgqPtxWMz9lVUOhVTyhVTkcp3ExnKVbXGbXPDxWnJLtpT4hnKAhqJ1ypzywXPx6PtxWPDyjpzyhqPtvKQNmZ1fjBlVep3ElXUWuozEcoaDbZmVfZmLcXFfvBmDjoIkhVvgmqUVbpT51oFxeVvQvudjtVPVepT4cPtxWPDyjoaIgoTymqP5upUOyozDbpT51oFxXPDxWPKOhqJ0eCGRXPDxWPKOfnKA0YzSjpTIhMPujovxXPDycMvOho3DtpTkcp3DtBtbWPDyjpzyhqPtvKT5pZQZmJmR7ZmR7AQOgH0yAVTkcp3DtnKZtMJ1jqUxhYxMcpaA0oUxtLJExVTRtp2ygVSkhVvxXPDyyoUAyBtbWPDy3nTyfMFOHpaIyBtbWPDxWqUW5BtbWPDxWPKAfL3E0MS9jovN9VTyhqPucoaO1qPtvKT5GMJkyL3DtLFOhqJ1vMKVtMz9lVUWyoJ92MFNtBvNvXFxXPDxWPDycMvOmoTA0qTEspT4toz90VTyhVUOhqJ1fnKA0BtbWPDxWPDyjpzyhqPtvKQNmZ1fjBmZkBmDjoF4hYzyhqzSfnJDtp2IfMJA0nJ9hYv4hVPVcPtxWPDxWPJAioaEcoaIyPtxWPDxWLaWyLJfXPDxWPJI4L2IjqPOJLJk1MHIlpz9lBtbWPDxWPKOlnJ50XPWpZQZmJmN7ZmR7AQOgYv4hnJ52LJkcMP4hYvNvXDbWPDyjLKEbVQ0tp3ElXUOfnKA0J3AfL3E0MS9jov0kKFxXPDxWpz10pzIyXUOuqTtcPtxWPJyzVT5iqPOyrTymqUZbpTS0nPx6PtxWPDymnTIfoPtvL2kyLKVvXFN7VTWuoz5ypvtcPtxWPDyjpzyhqPtvKQNmZ1fjBlVep3ElXUWuozEcoaDbZmVfZmLcXFfvBmDjoIAcoFNvX3OuqTteVvOlMJ1iqzIxYv4hVPVcPtxWPJIfp2H6PtxWPDyjpzyhqPtvKQNmZ1fjBmZkBmDjoF4hYaAioKEbnJ5aVUqlo25aYv4hVvxXPDyvpzIunjbWPtxXPJyzVTAbo2ywMFN9CFN0BtbWPKAbMJkfXPWmnPO1ozyhp3EuoTjhp2tvXDbWPJWlMJSePtxXPDbWMJkmMGbXPDyjpzyhqPtvKQNmZ1fjBmZkBmDjoF4hYzyhqzSfnJDtp2IfMJA0nJ9hYv4hVPVc'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))