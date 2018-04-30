package mallinone.ricardogotheil.com.mallinone

import android.content.Context
import android.content.Intent
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import kotlinx.android.synthetic.main.local_layout.view.*

class LocalAdapter(val homeFeed: HomeFeed2, context: Context): RecyclerView.Adapter<CustomViewHolder2>() {

    var mContext = context

    override fun getItemCount(): Int {
        return homeFeed.results.count()
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CustomViewHolder2 {

        val layoutInflater = LayoutInflater.from(parent?.context)
        val cellForRow = layoutInflater.inflate(R.layout.local_layout, parent, false)
        return CustomViewHolder2(cellForRow)
    }

    override fun onBindViewHolder(holder: CustomViewHolder2, position: Int) {
        val locals = homeFeed.results.get(position)
        holder?.view?.textView_local_name?.text = locals.name
        holder.setOnCustomItemClickListener(object: CustomClickListener2{
            override fun onCustomItemClickListener(view: View, pos: Int) {
                //Toast.makeText(mContext, "Name", Toast.LENGTH_LONG).show()
                val intent = Intent(view.context, LocalActivity::class.java)
                view.context.startActivity(intent)
            }
        })
    }
}

class CustomViewHolder2(val view: View): RecyclerView.ViewHolder(view), View.OnClickListener {
    var customClickListener2: CustomClickListener2?= null
    init {
        itemView.setOnClickListener(this)
    }

    fun setOnCustomItemClickListener(itemClickListener: CustomClickListener2) {
        this.customClickListener2 = itemClickListener
    }

    override fun onClick(v: View?) {
        this.customClickListener2!!.onCustomItemClickListener(v!!, adapterPosition)
    }
}

interface CustomClickListener2 {

    fun onCustomItemClickListener(view: View, pos: Int)
}