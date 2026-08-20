package com.yaolang.app;
import android.app.Activity;
import android.graphics.Color;
import android.graphics.Typeface;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.Gravity;
import android.view.View;
import android.widget.*;
public class MainActivity extends Activity {
    private LinearLayout ml;
    private TextView log;
    private EditText input;
    private Handler h;
    @Override protected void onCreate(Bundle s) {
        super.onCreate(s);
        h = new Handler(Looper.getMainLooper());
        ml = new LinearLayout(this);
        ml.setOrientation(LinearLayout.VERTICAL);
        ml.setPadding(dp(16),dp(16),dp(16),dp(16));
        ml.setBackgroundColor(0xFFF5F5F5);
        addTitle("YaoLang Android",24,0xFF333333,true);
        addTitle("YaoLang v0.1.0",14,0xFF888888,false);
        spacer(20);
        addCard("Welcome to YaoLang App\n\n"
            + "Powered by YaoLang (Yao Yu) Programming Language.\n"
            + "Keywords are 100% Chinese.\n\n"
            + "Build:\n"
            + "1. YaoLang compiler (yaolang.c)\n"
            + "2. C code -> gcc -> native\n"
            + "3. d8 -> DEX\n"
            + "4. Package -> Sign -> APK");
        spacer(12);
        LinearLayout r1=row();
        r1.addView(mkBtn("Fib(20)",0xFF4CAF50,()->out("fib(20)="+fib(20))));
        r1.addView(mkBtn("Fact(12)",0xFF2196F3,()->out("12!="+fact(12))));
        ml.addView(r1);
        LinearLayout r2=row();
        r2.addView(mkBtn("Time",0xFF9C27B0,()->{long t=System.currentTimeMillis();
            out(String.format("%02d:%02d:%02d",(t/3600000)%24,(t/60000)%60,(t/1000)%60));}));
        r2.addView(mkBtn("Device",0xFFFF9800,()->
            out(android.os.Build.MODEL+" "+android.os.Build.VERSION.RELEASE)));
        ml.addView(r2);
        spacer(16);
        LinearLayout ir=row();
        input=new EditText(this);
        input.setHint("Enter name...");
        input.setTextSize(16);
        input.setSingleLine(true);
        LinearLayout.LayoutParams ep=new LinearLayout.LayoutParams(0,dp(48),1f);
        ep.setMargins(0,0,dp(8),0);
        input.setLayoutParams(ep);
        ir.addView(input);
        ir.addView(mkBtn("Say Hi!",0xFF00BCD4,()->{
            String n=input.getText().toString().trim();
            if(n.isEmpty()) n="Friend";
            out("Hello, "+n+"!\nWelcome to YaoLang world!");}));
        ml.addView(ir);
        spacer(16);
        addTitle("Output",14,0xFF888888,false);
        log=new TextView(this);
        log.setTextSize(13);
        log.setTextColor(0xFF1B5E20);
        log.setBackgroundColor(0xFFE8F5E9);
        log.setPadding(dp(12),dp(8),dp(12),dp(8));
        log.setTypeface(Typeface.MONOSPACE);
        log.setText("Ready");
        ml.addView(log);
        spacer(16);
        addTitle("YaoLang v0.1.0-alpha",11,0xFFAAAAAA,false);
        ScrollView sv=new ScrollView(this);
        sv.addView(ml);
        setContentView(sv);
        out("App started OK");
    }
    void addTitle(String t,int s,int c,boolean b){
        TextView tv=new TextView(this);tv.setText(t);tv.setTextSize(s);tv.setTextColor(c);
        if(b)tv.setTypeface(null,Typeface.BOLD);
        tv.setGravity(Gravity.CENTER);
        LinearLayout.LayoutParams p=new LinearLayout.LayoutParams(-1,-2);
        p.setMargins(0,0,0,b?dp(24):dp(4));
        tv.setLayoutParams(p);ml.addView(tv);
    }
    void addCard(String t){
        TextView tv=new TextView(this);tv.setText(t);tv.setTextSize(14);tv.setTextColor(0xFF555555);
        tv.setLineSpacing(dp(4),1.2f);
        LinearLayout.LayoutParams p=new LinearLayout.LayoutParams(-1,-2);
        p.setMargins(dp(4),dp(4),dp(4),dp(12));
        tv.setLayoutParams(p);ml.addView(tv);
    }
    void spacer(int d){View v=new View(this);v.setMinimumHeight(dp(d));ml.addView(v);}
    LinearLayout row(){
        LinearLayout r=new LinearLayout(this);
        r.setOrientation(LinearLayout.HORIZONTAL);
        r.setGravity(Gravity.CENTER);
        LinearLayout.LayoutParams p=new LinearLayout.LayoutParams(-1,-2);
        p.setMargins(0,dp(4),0,0);r.setLayoutParams(p);return r;
    }
    Button mkBtn(String t,int c,Runnable a){
        Button b=new Button(this);b.setText(t);b.setTextSize(12);b.setTextColor(Color.WHITE);
        b.setBackgroundColor(c);b.setTypeface(null,Typeface.BOLD);
        b.setOnClickListener(v->a.run());
        LinearLayout.LayoutParams p=new LinearLayout.LayoutParams(0,dp(40),1f);
        p.setMargins(dp(4),0,dp(4),0);b.setLayoutParams(p);return b;
    }
    void out(String t){h.post(()->log.setText(log.getText()+"\n"+t));}
    int dp(int v){return(int)(v*getResources().getDisplayMetrics().density);}
    long fib(long n){return n<=1?n:fib(n-1)+fib(n-2);}
    long fact(long n){return n<=1?1:n*fact(n-1);}
}
