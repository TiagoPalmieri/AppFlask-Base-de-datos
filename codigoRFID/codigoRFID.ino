#include <SPI.h>

#include <SoftwareSerial.h>

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN_1  9       // Pin 9 para el reset del RC522 #1
#define SS_PIN_1   10      // Pin 10 para el SS (SDA) del RC522 #1
#define RST_PIN_2  6       // Pin 6 para el reset del RC522 #2
#define SS_PIN_2   2       // Pin 2 para el SS (SDA) del RC522 #2
#define BUZZER_PIN 7

MFRC522 reader1(SS_PIN_1, RST_PIN_1); // Creamos el objeto para el RC522 #1
MFRC522 reader2(SS_PIN_2, RST_PIN_2); // Creamos el objeto para el RC522 #2

void setup() {
  Serial.begin(9600); // Iniciamos la comunicación serial
  SPI.begin();        // Iniciamos el Bus SPI
  reader1.PCD_Init(); // Iniciamos el lector RC522 #1
  reader2.PCD_Init(); // Iniciamos el lector RC522 #2
  Serial.println("Control Inicializado ...");
}

void loop() {
  noTone(BUZZER_PIN);

  // Verificamos si se ha detectado alguna tarjeta en el lector #1
  if (reader1.PICC_IsNewCardPresent() && reader1.PICC_ReadCardSerial()) {
    tone(BUZZER_PIN, 440);
    Serial.print("Card UID (Lector 1): ");
    printCardUID(reader1.uid);
    reader1.PICC_HaltA(); // Terminamos la lectura de la tarjeta actual en el lector #1
  }

  // Verificamos si se ha detectado alguna tarjeta en el lector #2
  if (reader2.PICC_IsNewCardPresent() && reader2.PICC_ReadCardSerial()) {
    tone(BUZZER_PIN, 880);
    Serial.print("Card UID (Lector 2): ");
    printCardUID(reader2.uid);
    reader2.PICC_HaltA(); // Terminamos la lectura de la tarjeta actual en el lector #2
  }
}

void printCardUID(MFRC522::Uid uid) {
  for (byte i = 0; i < uid.size; i++) {
    Serial.print(uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(uid.uidByte[i], HEX);
  }
  Serial.println();
}