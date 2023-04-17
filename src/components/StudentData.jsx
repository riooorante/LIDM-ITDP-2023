import Mario from "../assets/images/H075.jpg";

const StudentData = () => {
  return (
    <div class="student-data-container">
      <div className="student-data-title">
        <p>STUDENT PROFILE PAGE</p>
      </div>
      <div class="photo-container">
        <div class="photo">
          <img src={Mario} alt="Mario" />
        </div>
        <div class="photo-text-container">
          <p class="name">Mario Valerian</p>
          <p class="nim">C211221890</p>
          <p class="program-studi">Kedokteran</p>
        </div>
      </div>
      <table>
        <thead>
          <tr>
            <th>No.</th>
            <th>Nilai</th>
            <th>IP</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>80</td>
            <td>3.5</td>
          </tr>
          <tr>
            <td>2</td>
            <td>85</td>
            <td>3.7</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default StudentData;
