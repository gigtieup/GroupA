from flask import re
@app.route('/my_form', methods=['POST'])
def my_form():

    if request.method == 'POST':
        conn = create_connection("gast.db") 

        c = conn.cursor()
        guest_vnaam = request.form.get('Voornaam')
        guest_anaam = request.form.get('Achternaam')
        guest_cnaam = request.form.get('Bedrijfsnaam')
        guest_datum = request.form.get('Datum')

        try:
            sql = ("INSERT INTO databasename.tablename (columnName,columnName,columnName,columnName Ci) VALUES (%s, %s, %s, %s)")
            c.execute(sql,(guest_vnaam, guest_anaam, guest_cnaam,  guest_datum))
            conn.commit() 
            #or "conn.commit()" (one of the two)
            return redirect('/')
        except:
            return 'Er ging iets fout met het opslaan van uw gegevens'
        finally:
            conn.close()