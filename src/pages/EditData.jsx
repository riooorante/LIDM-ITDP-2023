import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { getDataSiswa } from "../api";

const Siswa = () => {
  const [siswa, setSiswa] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await getDataSiswa();
      setSiswa(result);
    };
    fetchData();
  }, []);

  return (
    <div className="container">
      <h1>Data Siswa</h1>
      <table className="table">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">Nama</th>
            <th scope="col">Alamat</th>
            <th scope="col">No HP</th>
            <th scope="col">Aksi</th>
          </tr>
        </thead>
        <tbody>
          {siswa.map((data, index) => (
            <tr key={index}>
              <th scope="row">{index + 1}</th>
              <td>{data.nama}</td>
              <td>{data.alamat}</td>
              <td>{data.nohp}</td>
              <td>
                <Link to={`/siswa/edit/${data.id}`} className="btn btn-warning me-2">
                  Edit
                </Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <Link to="/siswa/tambah" className="btn btn-primary">
        Tambah Data
      </Link>
    </div>
  );
};

export default Siswa;
