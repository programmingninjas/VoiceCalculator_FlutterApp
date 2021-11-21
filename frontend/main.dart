import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:async';

void main() {
  runApp(const MaterialApp(
    home: MyApp(),
  ));
}

class MyApp extends StatefulWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  _MyAppState createState() => _MyAppState();
}
class _MyAppState extends State<MyApp> {
  TextEditingController voicetext = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Voice Calculator"),
          backgroundColor: const Color(0xff14238e),
          foregroundColor: Colors.white,
        ),
        backgroundColor: const Color(0xff080e39),
        body: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Padding(padding: const EdgeInsets.all(20),
                child: Image.network(
                    "https://github.com/programmingninjas/Voice-Calculator/blob/main/static/logo.jpg?raw=true"),)
              ,
              Padding(
                padding: const EdgeInsets.all(20),
                child: TextField(
                  controller: voicetext,
                  autofocus: true,
                  style: const TextStyle(
                    color: Colors.white,
                  ),
                  decoration: const InputDecoration(
                      hintStyle: TextStyle(color: Colors.white38),
                      labelStyle: TextStyle(
                          color: Color(0xff213cff), fontSize: 25),
                      enabledBorder: OutlineInputBorder(
                        borderSide: BorderSide(
                            color: Color(0xff14238e)
                        ),
                      ),
                      focusedBorder: OutlineInputBorder(
                          borderSide: BorderSide(
                              color: Colors.white
                          )
                      ),
                      labelText: 'Spoken Words',
                      hintText:
                      'Tap the keyboard microphone to start'
                  ),
                ),
              ),
              Padding(padding: const EdgeInsets.all(20), child: ElevatedButton(
                onPressed: () {
                  String text = voicetext.text;
                  Future sendText(String url) async {
                    http.Response response = await http.get(Uri.parse(url));
                    showAlertDialog(BuildContext context,answer) {
                      // Create button
                      Widget okButton = TextButton(
                        child: const Text("OK"),
                        onPressed: () {
                          Navigator.of(context).pop();
                        },
                      );

                      // Create AlertDialog
                      AlertDialog alert = AlertDialog(
                        title: const Text("Result!"),
                        content: Text(answer),
                        actions: [
                          okButton,
                        ],
                      );

                      // show the dialog
                      showDialog(
                        context: context,
                        builder: (BuildContext context) {
                          return alert;
                        },
                      );
                    }
                    showAlertDialog(context, response.body);
                  }
                  sendText("http://10.0.2.2:5000/api?text=" + text);
                },
                child: const Text("Calculate"),
                style: ButtonStyle(
                    backgroundColor: MaterialStateProperty.all<Color>(
                        const Color(0xff213cff)),
                    foregroundColor: MaterialStateProperty.all<Color>(
                        Colors.white),
                    overlayColor: MaterialStateProperty.all<Color>(Colors.grey),
                    minimumSize: MaterialStateProperty.all<Size>(
                        const Size(120, 50)),
                    shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                        RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(30)))
                ),),)
            ])
    );
  }
}

