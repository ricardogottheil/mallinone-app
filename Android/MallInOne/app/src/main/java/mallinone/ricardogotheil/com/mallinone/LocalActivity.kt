package mallinone.ricardogotheil.com.mallinone

import android.content.Intent
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v7.widget.LinearLayoutManager
import com.google.gson.GsonBuilder
import kotlinx.android.synthetic.main.activity_local.*
import okhttp3.*
import java.io.IOException

class LocalActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_local)

        recyclerView_main2.layoutManager = LinearLayoutManager(this)
        //recyclerView_main.adapter = MallAdapter()

        button_mallMap.setOnClickListener {
            val mapa = Intent(this, MapsActivity::class.java)
            startActivity(mapa)
        }

        fetchJson()
    }

    fun fetchJson() {
        val url = "http://mallinone.tk/api/v1/local/?format=json"

        val request = Request.Builder().url(url).build()

        val client = OkHttpClient()
        client.newCall(request).enqueue(object: Callback {
            override fun onResponse(call: Call?, response: Response?) {
                val body = response?.body()?.string()
                println(body)

                val gson = GsonBuilder().create()

                val homeFeed = gson.fromJson(body, HomeFeed2::class.java)

                runOnUiThread {
                    recyclerView_main2.adapter = LocalAdapter(homeFeed, applicationContext)
                }
            }

            override fun onFailure(call: Call?, e: IOException?) {
                println("Fail")

            }
        })
    }

}

class HomeFeed2(val results: List<Local>)

