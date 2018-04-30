package mallinone.ricardogotheil.com.mallinone

import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.support.v7.widget.LinearLayoutManager
import com.google.android.gms.common.api.PendingResults
import com.google.gson.GsonBuilder
import kotlinx.android.synthetic.main.activity_malls.*
import okhttp3.*
import java.io.IOException

class MallsActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_malls)

        recyclerView_main.layoutManager = LinearLayoutManager(this)
        //recyclerView_main.adapter = MallAdapter()

        fetchJson()
    }

    fun fetchJson() {
        val url = "http://mallinone.tk/api/v1/mall/?format=json"

        val request = Request.Builder().url(url).build()

        val client = OkHttpClient()
        client.newCall(request).enqueue(object: Callback {
            override fun onResponse(call: Call?, response: Response?) {
                val body = response?.body()?.string()
                println(body)

                val gson = GsonBuilder().create()

                val homeFeed = gson.fromJson(body, HomeFeed::class.java)

                runOnUiThread {
                    recyclerView_main.adapter = MallAdapter(homeFeed, applicationContext)
                }
            }

            override fun onFailure(call: Call?, e: IOException?) {
                println("Fail")

            }
        })
    }

}

class HomeFeed(val results: List<Mall>)
