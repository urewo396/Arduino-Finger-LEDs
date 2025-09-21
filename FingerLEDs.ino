
int ledPins[] = { 8, 9, 10, 11, 12 };

void setup() {
	for (int i = 0; i < 5; i++) {
		pinMode(ledPins[i], OUTPUT);
	}
	Serial.begin(9600);
}

void loop() {
	if (Serial.available()) {
		int num = Serial.readStringUntil('\n').toInt();
		for (int i = 0; i < 5; i++) {
			if (i < num) digitalWrite(ledPins[i], HIGH);
			else digitalWrite(ledPins[i], LOW);
		}
	}
}