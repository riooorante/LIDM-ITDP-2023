import { useState, useEffect } from "react";
import { getDataSiswa, searchSiswa } from "../api";
import { useNavigate } from "react-router-dom";
// import { storage } from "../firebase";

import Loader from "./Loader";

import testImage from "../assets/images/placeholder-3x4.gif";
import Mario from '../assets/images/H075.jpg';
import Kelvin from '../assets/images/H020.jpg';

const AttendData = () => {
  const [initialData, setInitialData] = useState([]);
  const [dataSiswa, setDataSiswa] = useState(initialData);
  const [isLoading, setIsLoading] = useState(false);

  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      setIsLoading(true);
      try {
        const response = await getDataSiswa();
        setDataSiswa(response);
        setInitialData(response);
      } catch (error) {
        console.log(error);
      } finally {
        setIsLoading(false);
      }
    };
    fetchData();
  }, []);

  const siswaList = dataSiswa.map((siswa, i) => {
    return (
      <div key={i} className="data-wrapper">
        {/* <div className="data-siswa-header">{siswa.nama}</div> */}
        <div className="data-siswa-body-container">
          <img src={siswa.nama === "Mario Valerian" ? Mario : siswa.nama === "Kelvin Leonardo" ? Kelvin : testImage} alt="Foto siswa" className="data-siswa-foto" />
          {/* <img src={siswa.foto} alt="Foto siswa" className="data-siswa-foto" /> */}
          <div className="data-siswa-text-container">
            <div className="data-siswa-text">
              <p>{siswa.nama}</p>
              <p>{siswa.ID}</p>
              <p>{siswa.jurusan}</p>
            </div>
          </div>
        </div>
        <div className="data-siswa-footer-container">
          <div className="data-siswa-waktu">Waktu Hadir : {siswa.lastScan}</div>
          <div className="data-siswa-kehadiran">
            Kehadiran : {siswa.kehadiran}
          </div>
        </div>
        <div className="data-view-button-container">
          <button
            onClick={() =>
              navigate("/attendinfo/studentinformation")
            }
          >
            View
          </button>
        </div>
        {/* <br /> */}
      </div>
    );
  });

  const findSiswa = async (query) => {
    if (query.length > 2) {
      setIsLoading(true);
      const result = await searchSiswa(query);
      setDataSiswa(result);
      setIsLoading(false);
    } else {
      setDataSiswa(initialData);
    }
  };

  return (
    <div className="attend-page">
      <header className="attend-header">
        <p>Daftar Siswa</p>
        <input
          type="text"
          placeholder="Cari nama siswa..."
          className="data-search"
          onChange={({ target }) => findSiswa(target.value)}
        />
      </header>
      <div className="data-container">
        {isLoading ? (
          <Loader />
        ) : dataSiswa.length > 0 ? (
          siswaList
        ) : (
          <p>Data tidak ditemukan</p>
        )}
      </div>
    </div>
  );
};

export default AttendData;
