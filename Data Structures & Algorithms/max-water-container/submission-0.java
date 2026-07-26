class Solution {
    public int maxArea(int[] height) {
        Scanner sc=new Scanner(System.in);
        int n=height.length;
        int i=0;
        int j=n-1;
        int max_water=0;
        while(i<j){
            int h;
            if(height[i]<height[j]){
                h=height[i];
            }
            else{
                h=height[j];
            }
            int width=j-i;
            int area=h*width;
            if(area>max_water){
                max_water=area;
            }
            if(height[i]<height[j]){
                i+=1;
            }
            else{
                j-=1;
            }
            
            
        }
        return max_water;

        
    }
}
