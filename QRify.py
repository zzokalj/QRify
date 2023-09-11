import os
import qrcode
import pandas as pd
import datetime

def generate_qr_codes(data, language, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for _, row in data.iterrows():
        vcard_data = f"BEGIN:VCARD\nVERSION:3.0\nN:{row['Prezime']};{row['Ime']};;;\nTITLE:{row['titula']}\nORG:{row['radno mjesto']}\nTEL:{row['telefon']}\nTEL:{row['mobitel']}\nEMAIL:{row['mail']}\nADR:{row['adresa']}\nURL:{row['web']}\nEND:VCARD"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        qr.add_data(vcard_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")

        filename = os.path.join(output_folder, f"QR {row['Ime']} {row['Prezime']} {language}.png")
        img.save(filename)

def main():
    print("QRify v1.0 -", datetime.date.today())
    print("Copyright by Zeno Žokalj, 2023. All rights reserved.")

    language = input("Choose the language (Croatian/English): ").lower().strip()

    if language not in ['croatian', 'english']:
        print("Invalid language selection. Please choose Croatian or English.")
        return

    data_folder = input(f"Enter the path to the {language} CSV file (e.g., contact_data_{language.upper()}.csv): ")

    try:
        data = pd.read_csv(data_folder, encoding='iso-8859-1', delimiter=';')
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {str(e)}")
        return

    output_folder = os.path.join(os.path.dirname(data_folder), 'HAKOM QRify', language.upper())
    generate_qr_codes(data, language, output_folder)

    continue_with_other_language = input("Do you want to proceed with the other language? (yes/no): ").lower().strip()

    if continue_with_other_language == 'yes':
        other_language = 'english' if language == 'croatian' else 'croatian'
        data_folder = input(f"Enter the path to the {other_language} CSV file (e.g., contact_data_{other_language.upper()}.csv): ")

        try:
            data = pd.read_csv(data_folder, encoding='iso-8859-1', delimiter=';')
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {str(e)}")
            return

        output_folder = os.path.join(os.path.dirname(data_folder), 'HAKOM QRify', other_language.upper())
        generate_qr_codes(data, other_language, output_folder)

    print("Thank you for using QRify! Buy Zeno a coffee. ;)")

if __name__ == "__main__":
    main()
