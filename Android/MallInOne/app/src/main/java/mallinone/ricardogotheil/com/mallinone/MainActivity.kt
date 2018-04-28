package mallinone.ricardogotheil.com.mallinone

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        buttonGoogleMaps.setOnClickListener {
            val mapa = Intent(this, MapsActivity::class.java)
            startActivity(mapa)
        }

        buttonMalls.setOnClickListener {
            val malls = Intent(this, MallsActivity::class.java)
            startActivity(malls)
        }

        buttonSearchs.setOnClickListener {
            val searchs = Intent(this, SearchesActivity::class.java)
            startActivity(searchs)
        }
    }
}
