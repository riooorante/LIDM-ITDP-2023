import firebase from "firebase/app";
import "firebase/storage";

const firebaseConfig = {
  apiKey: process.env.REACT_APP_DB_SISWA_BASEURL,
  storageBucket: "pilajara-d8d3f.appspot.com",
};

firebase.initializeApp(firebaseConfig);

const storage = firebase.storage();

export { storage };
