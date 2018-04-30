package mallinone.ricardogotheil.com.mallinone

import android.content.Context
import android.content.Intent
import android.support.v4.content.ContextCompat.startActivity
import android.support.v7.app.AppCompatActivity
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Toast
import kotlinx.android.synthetic.main.mall_layout.view.*

class MallAdapter(val homeFeed: HomeFeed, context: Context): RecyclerView.Adapter<CustomViewHolder>() {

    var mContext = context

    override fun getItemCount(): Int {
        return homeFeed.results.count()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CustomViewHolder {

        val layoutInflater = LayoutInflater.from(parent?.context)
        val cellForRow = layoutInflater.inflate(R.layout.mall_layout, parent, false)
        return CustomViewHolder(cellForRow)
    }

    override fun onBindViewHolder(holder: CustomViewHolder, position: Int) {
        val malls = homeFeed.results.get(position)
        holder?.view?.textView_mall_name?.text = malls.name
        holder.setOnCustomItemClickListener(object: CustomClickListener{
            override fun onCustomItemClickListener(view: View, pos: Int) {
                //Toast.makeText(mContext, "Name", Toast.LENGTH_LONG).show()
                val intent = Intent(view.context, LocalActivity::class.java)
                view.context.startActivity(intent)
            }
        })
    }
}

class CustomViewHolder(val view: View): RecyclerView.ViewHolder(view), View.OnClickListener {
    var customClickListener: CustomClickListener?= null
    init {
        itemView.setOnClickListener(this)
    }

    fun setOnCustomItemClickListener(itemClickListener: CustomClickListener) {
        this.customClickListener = itemClickListener
    }

    override fun onClick(v: View?) {
        this.customClickListener!!.onCustomItemClickListener(v!!, adapterPosition)
    }
}

interface CustomClickListener {

    fun onCustomItemClickListener(view: View, pos: Int)
}
