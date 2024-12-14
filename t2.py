import threading

creneau_reserve = 0
patient_recu = 0
encaissement = 0
verrou_creneau = threading.Lock()
verrou_patient = threading.Lock()


def prendre_rdv0():
    global creneau_reserve, patient_recu, encaissement
    for rdv in range(100000):
        verrou_creneau.acquire()
        nombre_creneau = creneau_reserve
        verrou_patient.acquire()
        nombre_patient = patient_recu
        creneau_reserve = nombre_creneau + 1
        verrou_creneau.release()
        patient_recu = nombre_patient + 1
        verrou_patient.release()
    encaissement = encaissement + 25 * 100000


def prendre_rdv():
    global creneau_reserve, patient_recu, encaissement
    for rdv in range(1000000):
        nombre_creneau = creneau_reserve
        nombre_patient = patient_recu
        creneau_reserve = nombre_creneau + 1
        patient_recu = nombre_patient + 1
    encaissement = encaissement + 25 * 100000


def prendre_rdv2():
    global creneau_reserve, patient_recu, encaissement
    for rdv in range(1000000):
        nombre_creneau = creneau_reserve
        nombre_patient = patient_recu
        creneau_reserve = nombre_creneau + 1
        patient_recu = nombre_patient + 1
    encaissement = encaissement + 25 * 100000


def prendre_rdv3():
    global creneau_reserve, patient_recu, encaissement
    for rdv in range(1000000):
        nombre_creneau = creneau_reserve
        nombre_patient = patient_recu
        creneau_reserve = nombre_creneau + 1
        patient_recu = nombre_patient + 1
    encaissement = encaissement + 25 * 100000


prendre_rdv()
prendre_rdv2()
prendre_rdv3()
print(creneau_reserve, patient_recu, encaissement)
