#include <stdio.h>
#include <math.h>
#define PI 3.14159265

void fft(float *in_real, float *in_img,int leng,int N, float *out_real, float* out_img)
{
    float sum_real,sum_img,cc,ss,temp_real,temp_img;
    int k,n;
    for(k=0;k<N;k++)
    {
        sum_real=0;
        sum_img=0;
        for(n=0;n<N;n++)
        {
            if (n<leng)
            {
                temp_real=in_real[n];
                temp_img=in_img[n];
            }
            else
            {
                temp_real=0;
                temp_img=0;
            }
            cc=cos((2*PI*k*n)/N);
            ss=-sin((2*PI*k*n)/N);

            sum_real=sum_real+(cc*temp_real-ss*temp_img);
            sum_img=sum_img+(cc*temp_img+ss*temp_real);
        }
        out_real[k]=sum_real;
        out_img[k]=sum_img;
    }
}

void ifft(float *in_real, float *in_img,int leng,int N, float *out_real, float* out_img)
{
    float sum_real,sum_img,cc,ss;
    int k,n;
    for(k=0;k<N;k++)
    {
        sum_real=0;
        sum_img=0;
        for(n=0;n<N;n++)
        {
            cc=cos((2*PI*k*n)/N);
            ss=sin((2*PI*k*n)/N);

            sum_real=sum_real+(cc*in_real[n]-ss*in_img[n]);
            sum_img=sum_img+(cc*in_img[n]+ss*in_real[n]);
        }
        out_real[k]=sum_real/N;
        out_img[k]=sum_img/N;
    }
}

void circ(int L, float *input_real,float *input_img, float *h_real, float*h_img, float *fin_real, float *fin_img, int inp_size, int flt_size)
{
    int i,j;
    /*
    int L=22;
    float h_real[]={-0.236332264877126,-0.981265867280092,-0.769588232293259,-1.23612287548513,-0.0502147066337280,-0.388664002173484,-0.311945110971044,0.221364699595723,-0.297324985059649,-1.69719472604544,-0.598709290297369,-0.523346811663220};
    float h_img[]={0,0,0,0,0,0,0,0,0,0,0,0};
    float input_real[]={0.637859263803680,-0.565981624425496,-0.0161376263168116,0.622322565335203,0.533436361755158,-0.389340755635536,-1.27166778821102,0.272601061641828,0.317468464887969,1.49836827592653,-1.55380079114989,-0.354291622942114,0.434227622152402,-0.101478020404053,2.02876798537404,-0.367211878382280,-2.36377484799189,0.729858345361788,-1.39902075927839,1.31488703713417,0.403825374672520,-0.344166227763040,-0.980064257303274,1.85734541988710,0.309538452610443,-0.489102726025899,-0.694883298029859,-0.180392601616680,1.25628334419483,1.91074361906141,0.0271929609615699,0.427129435909406,0.323364836070306,-1.64896803402833,0.140337987476392,-0.498042737564483,-0.427773025009844,-0.150874342982068,-2.89081005793843,-0.734542060860252,0.756215216777615,0.120792842515053,-0.515905646649828,-0.340858419139416,-1.07999215135802,-0.697388911993461,-0.582996712654704,-0.186125413462525,0.587960618326313,-0.0210413970099939,-0.0797613083325863,-0.835514785543058,0.978620077590616,0.235477911610788,0.566047741701346,0.219290253702244,0.807711012773034,1.51252674055338,-0.431633422559677,0.542560581041823,0.679299892415180,-0.00876691100522949,1.91194131724684,-0.978615854690519,-0.486129202750742,0.0778979515541982,0.0262010031147861,-0.222783873783366,-0.479705499184321,0.824587313965651,-0.0604033266660627,-0.806763830134446,1.71283780149174,0.912158351163016,1.48884170716556,-0.0267480490239616,1.91582423437216,0.919677108422164,-1.80809868670026,-1.26530785042028,0.583630615503540,-0.116187958486345,-0.143812268607298,1.07476955634590,1.70218903333732,0.391235336408327,0.127331572717260,2.25093102373581,-0.0106779312347955,-0.450549182359537,-0.595049578928503,-0.735669583528822,0.0816950618691643,-0.860856962954059,-1.85841048148535,-1.28488688986272,0.436202165643835,1.09128280274507,1.20260219158596,2.31286363180140,-1.08397934684503,1.36453423431839,0.0816802225411862,-0.467782226083564,-0.426379676073622,0.889624635043088,0.649750023315031,-1.80617860041516,1.02469639873353,0.825232263674637};
    float input_img[]={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    */
    /*
    for(i=0 ; i<350 ;i++)
    {
    printf("%d real is %f, img is %f \n",i,input_real[i],input_img[i]);
    }
    */
    /*
    int inp_size=sizeof(input_real)/4;
    int flt_size=sizeof(h_real)/4;
    */

    int x_pad_len=(flt_size+inp_size+L-1);

    /*X pad starts here*/
    float* x_pad_real = malloc((flt_size+inp_size+L-1) * sizeof(float));
    float* x_pad_img  = malloc((flt_size+inp_size+L-1) * sizeof(float));

    for(i=0;i<flt_size-1;i++)
    {
        x_pad_real[i]=0;
        x_pad_img[i]=0;
    }
    for(i=(flt_size-1) ;i<(flt_size-1+inp_size);i++)
    {
        x_pad_real[i]=input_real[i-flt_size+1];
        x_pad_img[i]=input_img[i-flt_size+1];
    }
    for(i=(flt_size-1+inp_size) ;i<(flt_size-1+inp_size+L);i++)
    {
        x_pad_real[i]=0;
        x_pad_img[i]=0;
    }
    /*X pad ends here checked*/

    /*
    int loop;
    if ( (flt_size+inp_size-L)%(L-flt_size+1) == 0)
    {
        loop=(flt_size+inp_size-L)/(L-flt_size+1);
        loop=loop+1;
    }
    else
    {
        loop=(flt_size+inp_size-L)/(L-flt_size+1);
        loop=loop+2;
    }
    float* fin_real = malloc((loop*(L-flt_size+1)) * sizeof(float));
    float* fin_img  = malloc((loop*(L-flt_size+1)) * sizeof(float));
    */

    float* h_real_fft = malloc(L * sizeof(float));
    float* h_img_fft  = malloc(L * sizeof(float));

    /*Before the loop according to MATLAB code*/
    fft(h_real,h_img,flt_size,L,h_real_fft,h_img_fft);

    float* inp_real_fft = malloc(L * sizeof(float));
    float* inp_img_fft  = malloc(L * sizeof(float));

    fft(x_pad_real,x_pad_img,L,L,inp_real_fft,inp_img_fft);

    float* temp_real = malloc(L * sizeof(float));
    float* temp_img  = malloc(L * sizeof(float));

    for(i=0 ; i<L ;i++)
    {
        temp_real[i]=(inp_real_fft[i]*h_real_fft[i])-(inp_img_fft[i]*h_img_fft[i]);
        temp_img[i]=(inp_img_fft[i]*h_real_fft[i])+(inp_real_fft[i]*h_img_fft[i]);
    }

    float* temp_fin_real = malloc(L * sizeof(float));
    float* temp_fin_img  = malloc(L * sizeof(float));

    ifft(temp_real,temp_img,L,L,temp_fin_real,temp_fin_img);

    for(i=(flt_size-1) ; i<L ;i++)
    {
        fin_real[i+1-flt_size]=temp_fin_real[i];
        fin_img[i+1-flt_size]=temp_fin_img[i];
    }

    free(inp_real_fft);
    free(inp_img_fft);
    free(temp_real);
    free(temp_img);
    free(temp_fin_real);
    free(temp_fin_img);
    /*End of before the loop according to MATLAB */

    /*The loop in the MATLAB code starts here*/
    int coun=0;
    for(i=L-1; i<=x_pad_len-L-1; i=i+L-flt_size+1)
    {
        printf("i value is %d \n",i);
        float* inp_real_fft = malloc(L * sizeof(float));
        float* inp_img_fft  = malloc(L * sizeof(float));

        fft(x_pad_real+(i-(flt_size-2)),x_pad_img+(i-(flt_size-2)),L,L,inp_real_fft,inp_img_fft);

        float* temp_real = malloc(L * sizeof(float));
        float* temp_img  = malloc(L * sizeof(float));

        for(j=0 ; j<L ;j++)
        {
        temp_real[j]=(inp_real_fft[j]*h_real_fft[j])-(inp_img_fft[j]*h_img_fft[j]);
        temp_img[j]=(inp_img_fft[j]*h_real_fft[j])+(inp_real_fft[j]*h_img_fft[j]);
        }

        float* temp_fin_real = malloc(L * sizeof(float));
        float* temp_fin_img  = malloc(L * sizeof(float));

        ifft(temp_real,temp_img,L,L,temp_fin_real,temp_fin_img);

        for(j=(flt_size-1) ; j<L ;j++)
        {
        fin_real[i-L+j+1]=temp_fin_real[j];
        fin_img[i-L+j+1]=temp_fin_img[j];
        }
    free(inp_real_fft);
    free(inp_img_fft);
    free(temp_real);
    free(temp_img);
    free(temp_fin_real);
    free(temp_fin_img);
    coun=coun+1;
    }

    /*
    for(i=0 ; i<(loop*(L-flt_size+1)) ;i++)
    {
    printf("%d real is %f, img is %f dot \n",i,fin_real[i],fin_img[i]);
    }
    */

    free(x_pad_real);
    free(x_pad_img);
    free(h_real_fft);
    free(h_img_fft);

    return 0;
}
