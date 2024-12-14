class AdresseIP:
    def __init__(self, adresse):
        """
        Entrées:
            - self, AdresseIP: objet AdresseIP
            - adresse, str: adresse IP sous la forme "a.b.c.d"
        Sorties: Aucune
        Rôle: Initialise l'adresse IP de l'objet AdresseIP
        """
        # On stocke l'adresse IP dans les propriétés de l'objet
        self.adresse = adresse

    def liste_octets(self):
        """
        Entrées: self, AdresseIP: objet AdresseIP
        Sorties: list de int: liste des octets de l'adresse IP
        Rôle: Renvoie la liste des octets de l'adresse IP
        """
        # On renvoie la liste des octets de l'adresse IP, convertis en entiers
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self):
        """
        Entrées: self, AdresseIP: objet AdresseIP
        Sorties: bool: True si l'adresse IP est réservée, False sinon
        Rôle: Vérifie si l'adresse IP est réservée
        """
        # Liste des adresses IP réservées
        reservees = ["192.168.0.0", "192.168.0.255"]

        # Renvoie le booléen indiquant si l'adresse est réservée ou non
        return self.adresse in reservees

    def adresse_suivante(self):
        """
        Entrées: self, AdresseIP: objet AdresseIP
        Sorties: AdresseIP: adresse IP suivante
        Rôle: Renvoie l'adresse IP suivante de l'adresse IP actuelle
        """
        # On récupère la liste des octets de l'adresse IP
        octets = self.liste_octets()
        # Si le dernier octet est 254, on ne peut pas avoir d'adresse suivante
        if octets[3] == 254:
            # On renvoie None
            return None

        # Sinon, on calcule le dernier octet de l'adresse suivante
        octet_nouveau = octets[3] + 1

        # On renvoie un objet AdresseIP avec l'adresse suivante
        return AdresseIP("192.168.0." + str(octet_nouveau))


# Exemple d'utilisation de la classe AdresseIP
# Initialisation d'adresses IP
adresse1 = AdresseIP("192.168.0.1")
adresse2 = AdresseIP("192.168.0.2")
adresse3 = AdresseIP("192.168.0.0")

# Tests des méthodes
print(adresse1.liste_octets())
print(adresse1.est_reservee())
print(adresse3.est_reservee())
print(adresse2.adresse_suivante().adresse)
