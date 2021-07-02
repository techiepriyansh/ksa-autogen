let adderNames;
let currentAdder;

window.addEventListener("load", async () => {
  adderNames = await eel.initialize()();
  currentAdder = adderNames[0];

  setupAdderSelection();

  setupEvents();

  // If the server stops, close the UI
  window.eel._websocket.addEventListener('close', e => window.close());
});
