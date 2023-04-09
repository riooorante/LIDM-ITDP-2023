import axios from "axios";

const baseUrl = process.env.REACT_APP_DB_SISWA_BASEURL;

export const getDataSiswa = async () => {
  try {
    const response = await axios.get(baseUrl);
    console.info(response.data);
    const dataArray = Object.values(response.data);
    // Dilakukan konversi ke tipe data Array karena akan menggunakan function .map() agar dapat melakukan perulangan untuk memunculkan semua data
    return dataArray;
  } catch (error) {
    console.error("There was a problem with the fetch operation:", error);
  }
};

export const searchSiswa = async (query) => {
  try {
    const response = await axios.get(
      `${baseUrl}?orderBy="nama"&equalTo="${query}"`
    );
    const dataArray = Object.values(response.data);
    return dataArray;
  } catch (error) {
    console.error("There was a problem with the search operation:", error);
  }
};
