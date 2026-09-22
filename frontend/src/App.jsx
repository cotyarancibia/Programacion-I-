import heroImg from './assets/hero.png'

function App() {
  return (
    <main className="home">
      <section className="hero" aria-labelledby="home-title">
        <div className="hero-content">
          <p className="eyebrow">Adopta, cuida y cambia una vida</p>
          <h1 id="home-title">Adopcion de Mascotas</h1>
          <p className="hero-copy">
            Home inicial del frontend React + Vite para conectar mascotas en adopcion con familias responsables.
          </p>
        </div>
        <img
          src={heroImg}
          className="hero-image"
          width="170"
          height="179"
          alt="Hero adopcion de mascotas"
        />
      </section>

      <section className="home-note" aria-label="Referencia de diseno">
        <h2>Bosquejo de referencia</h2>
        <p>La estructura visual final se guiara por <code>docs/bosquejo-home.png</code>.</p>
      </section>
    </main>
  )
}

export default App
