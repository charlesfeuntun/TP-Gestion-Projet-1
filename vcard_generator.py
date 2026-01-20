import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def generer_vcard(contact):
    """
    Génère un fichier vCard (.vcf) et une image de carte de visite (.png) 
    avec QR code intégré.
    
    Arguments:
        contact (dict): Un dictionnaire contenant les informations du contact.
    """
    # Recupération des données
    nom = contact.get('nom', '')
    prenom = contact.get('prenom', '')
    metier = contact.get('metier', '')
    tel = contact.get('telephone', '')
    email = contact.get('email', '')
    adresse = contact.get('adresse', '')
    site = contact.get('site', '')
    linkedin = contact.get('linkedin', '')

    # Construction du contenu vCard (Format 3.0)
    vcard_content = (
        "BEGIN:VCARD\n"
        "VERSION:3.0\n"
        f"N:{nom};{prenom};;;\n"
        f"FN:{prenom} {nom}\n"
        f"TITLE:{metier}\n"
        f"TEL;TYPE=CELL:{tel}\n"
        f"EMAIL:{email}\n"
        f"ADR;TYPE=HOME:;;{adresse};;;;\n"
    )
    if site:
        vcard_content += f"URL:{site}\n"
    if linkedin:
         vcard_content += f"X-SOCIALPROFILE;TYPE=linkedin:{linkedin}\n"
    vcard_content += "END:VCARD"
    
    # Création du nom de base
    base_filename = f"{prenom}_{nom}".replace(" ", "_").lower()
    
    # 1. Écriture du fichier .vcf
    vcf_filename = f"{base_filename}.vcf"
    with open(vcf_filename, "w", encoding="utf-8") as f:
        f.write(vcard_content)
    print(f"Fichier vCard généré : {vcf_filename}")

    # 2. Génération de l'image de la carte de visite
    
    # Dimensions et Couleurs
    width, height = 800, 450 # Format plus grand pour meilleure résolution
    
    # Palette "Midnight & Gold"
    col_bg_main = "#FFFFFF"        # Blanc pour la zone contenu
    col_sidebar = "#1A1A2E"        # Bleu très sombre pour coté gauche
    col_accent = "#E94560"         # Rouge/Rose vibrant pour les détails
    col_text_primary = "#16213E"   # Bleu sombre pour le texte
    col_text_secondary = "#533E85" # Violet/Gris pour les labels
    col_text_light = "#FFFFFF"     # Blanc pour texte sur fond sombre
    
    card_img = Image.new('RGB', (width, height), color=col_bg_main)
    draw = ImageDraw.Draw(card_img)
    
    # Design : Une barre latérale gauche large contenant Nom, Prénom, Métier
    sidebar_width = 320
    draw.rectangle([(0, 0), (sidebar_width, height)], fill=col_sidebar)
    
    # Tentative de chargement de polices avec tailles ajustées
    try:
        # Polices Windows standard
        font_name = ImageFont.truetype("arialbd.ttf", 45)     # Nom Gras
        font_job = ImageFont.truetype("ariali.ttf", 22)       # Métier Italique
        font_info_val = ImageFont.truetype("arial.ttf", 18)   # Info Valeur
        font_info_lbl = ImageFont.truetype("arialbd.ttf", 14) # Info Label
    except IOError:
        font_name = ImageFont.load_default()
        font_job = ImageFont.load_default()
        font_info_val = ImageFont.load_default()
        font_info_lbl = ImageFont.load_default()

    # --- CONTENU SIDEBAR (Logo + Identité) ---
    margin_left = 30
    y_cursor = 50 

    # Gestion du Logo facultatif
    logo_path = contact.get('logo_path')
    if logo_path and os.path.exists(logo_path):
        try:
            logo = Image.open(logo_path)
            # Redimensionnement max : Largeur sidebar - marges, Hauteur max 120
            logo.thumbnail((sidebar_width - (margin_left * 2), 120))
            
            # Gestion de la transparence (si png)
            mask = logo if logo.mode == 'RGBA' else None
            
            # Positionnement du logo
            card_img.paste(logo, (margin_left, y_cursor), mask)
            y_cursor += logo.height + 30
        except Exception as e:
            print(f"Erreur lors de l'ajout du logo: {e}")

    # Prénom
    draw.text((margin_left, y_cursor), prenom.upper(), font=font_name, fill=col_text_light)
    y_cursor += 50
    # Nom (Accentuation couleur ?)
    draw.text((margin_left, y_cursor), nom.upper(), font=font_name, fill=col_accent)
    y_cursor += 55
    
    # Ligne de séparation
    draw.line([(margin_left, y_cursor), (sidebar_width - 50, y_cursor)], fill="white", width=2)
    y_cursor += 20
    
    # Métier
    draw.text((margin_left, y_cursor), metier.upper(), font=font_job, fill=col_text_light)
    
    # --- CONTENU PRINCIPAL (Infos) ---
    x_info = sidebar_width + 40
    y_info = 60
    spacing = 60
    
    infos = [
        ("TÉLÉPHONE", tel),
        ("EMAIL", email),
        ("ADRESSE", adresse),
        ("SITE WEB", site),
        ("LINKEDIN", linkedin)
    ]
    
    for label, value in infos:
        if not value: continue
        
        # Petit rond décoratif
        draw.ellipse([(x_info, y_info + 5), (x_info + 10, y_info + 15)], fill=col_accent)
        
        # Label
        draw.text((x_info + 25, y_info), label, font=font_info_lbl, fill=col_text_secondary)
        
        # Valeur
        draw.text((x_info + 25, y_info + 20), value, font=font_info_val, fill=col_text_primary)
        
        y_info += spacing

    # --- QR CODE ---
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1,
    )
    qr.add_data(vcard_content)
    qr.make(fit=True)

    # QR Code avec couleurs personnalisées
    qr_img = qr.make_image(fill_color=col_sidebar, back_color="white")
    
    qr_size = 130
    qr_img = qr_img.resize((qr_size, qr_size))
    
    # Positionnement bas droite
    qr_x = width - qr_size - 30
    qr_y = height - qr_size - 30
    
    card_img.paste(qr_img, (qr_x, qr_y))
    
    # Petit cadre autour du QR Code
    draw.rectangle([(qr_x - 2, qr_y - 2), (qr_x + qr_size + 1, qr_y + qr_size + 1)], outline=col_sidebar, width=2)
    
    # Sauvegarde finale
    png_filename = f"{base_filename}_card.png"
    card_img.save(png_filename)
    print(f"Carte de visite moderne générée : {png_filename}")

if __name__ == "__main__":
    # Liste de contacts
    contacts = [
        {
            "nom": "Dufour",
            "prenom": "Enzo",
            "metier": "Etudiant en CyberSécurité",
            "telephone": "+33 5 31 53 05 09",
            "email": "contact@zebinet.tech",
            "adresse": "Rodez, France",
            "site": "zebinet.tech",
            "linkedin": "linkedin.com/in/zebinet-tech",
            "logo_path": "logo.jpeg"
        },
        {
            "nom": "Tournie",
            "prenom": "Luc",
            "metier": "Etudiant en CyberSécurité",
            "telephone": "+33 6 22 50 38 12",
            "email": "contact@luc-tournie.fr",
            "adresse": "Rodez, France",
            "site": "luc-tournie.fr",
            "linkedin": "linkedin.com/in/luc-tourni%C3%A9-862ba0224/",
            "logo_path": "logo.jpeg"
        },
        {
            "nom": "Doumbia",
            "prenom": "Noa",
            "metier": "Etudiant en CyberSécurité",
            "telephone": "+33 7 11 22 33 44",
            "email": "lycee@carnus.fr",
            "adresse": "Rodez, France",
            "site": "carnus.fr",
            "logo_path": "logo.jpeg"
        },
        {
            "nom": "Feuntun",
            "prenom": "Charles",
            "metier": "Etudiant en CyberSécurité",
            "telephone": "+33 7 11 22 33 44",
            "email": "lycee@carnus.fr",
            "adresse": "Rodez, France",
            "site": "carnus.fr",
            "logo_path": "logo.jpeg"
        }
    ]
    
    # Boucle pour générer une carte pour chaque contact
    for contact in contacts:
        generer_vcard(contact)
